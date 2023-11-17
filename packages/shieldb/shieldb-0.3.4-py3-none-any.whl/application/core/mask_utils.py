import json
import re
import signal


from sqlalchemy import text

CHUNK_SIZE = 500

patterns = {
            'tc': re.compile(r'\b(\d{4})[-.\s]?(\d{3})[-.\s]?(\d{4})\b'),
            'credit_card': re.compile(r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})\b'),
            'email': re.compile(r'\b[A-Za-z0-9._*%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'phone': re.compile(r'\b(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})\b'),
            'password': re.compile(r'(\b[A-Za-z0-9_-]+:)\s*\b([A-Za-z0-9_-]+)\b'),
            'url': re.compile(
                r'(https?://(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]['
                r'a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?://(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,'
                r'}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'),
        }


class ReplacesFunctions:
    def __init__(self):
        self.replace_url = ReplacesFunctions.replace_url()
        self.replace_password = ReplacesFunctions.replace_password()
        self.replace_email = ReplacesFunctions.replace_email()
        self.replace_credit_card_number = ReplacesFunctions.replace_credit_card_number()
        self.replace_phone_number = ReplacesFunctions.replace_phone_number()

    @staticmethod
    def replace_email(match):
        email = match.group(0)
        if len(email) > 2:
            parts = email.split("@")
            username = parts[0]
            new_email = email[0] + '*' * (len(username) - 2) + username[-1] + '@' + parts[1]
            return new_email
        else:
            return email

    @staticmethod
    def replace_phone_number(match):
        phone = match.group(0)
        response = phone[:-4] + '****'
        return response

    @staticmethod
    def replace_url(match):
        response = 'https://*****.com/***'
        return response

    @staticmethod
    def replace_credit_card_number(match):
        credit_card_number = match.group(0)
        response = credit_card_number[:4] + '*' * (len(credit_card_number) - 4)
        return response

    @staticmethod
    def replace_password(match):
        username = match.group(1)
        if len(match.group(2)) > 5:
            response = f"{username}******"
        else:
            response = f"{username}{match.group(2)}"
        return response


replace_functions = {
                'email': ReplacesFunctions.replace_email,
                'phone': ReplacesFunctions.replace_phone_number,
                'tc': ReplacesFunctions.replace_phone_number,
                'credit_card': ReplacesFunctions.replace_credit_card_number,
                'password': ReplacesFunctions.replace_password,
                'url': ReplacesFunctions.replace_url,
            }


class MaskUtils:
    def __init__(self, connection, args):
        self.connection = connection
        self.args = args

    def handler(signum, frame):
        print("User interrupted the process. Custom message here.")
        raise SystemExit

    def get_table_columns(self):
        result = self.connection.execute(text(
            f"SELECT column_name FROM information_schema.columns WHERE table_name = '{self.args.table}' AND column_name <> 'id'"
        ).params(table=self.args.table))

        return [row[0] for row in result]

    def delete_rows_in_chunks(self):

        signal.signal(signal.SIGINT, MaskUtils.handler)

        try:
            if not 0 <= self.args.percentage <= 100:
                print("Error: Percentage should be between 0 and 100.")
                return

            with self.connection.begin():
                total_rows = self.connection.execute(text(f'SELECT COUNT(*) FROM {self.args.table}')).scalar()
                rows_to_delete = int(total_rows * (self.args.percentage / 100))

                if rows_to_delete > 0:
                    chunks = (rows_to_delete + CHUNK_SIZE - 1) // CHUNK_SIZE

                    for chunk in range(chunks):
                        offset = chunk * CHUNK_SIZE
                        limit = min(CHUNK_SIZE, rows_to_delete - offset)

                        delete_query = text(
                            f'DELETE FROM {self.args.table} WHERE ctid IN (SELECT ctid FROM {self.args.table} ORDER BY RANDOM() OFFSET :offset LIMIT :limit)'
                        ).bindparams(offset=offset, limit=limit)
                        self.connection.execute(delete_query)
                        print(f"{chunk + 1} chunks processed.")

                    print(f"{self.args.percentage}% of data deleted from the {self.args.table} table.")
                else:
                    print(f"No rows to delete from the {self.args.table} table.")
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()

    def is_column_maskable(self, column_name):
        query = text(f'SELECT data_type FROM information_schema.columns WHERE table_name = :table_name AND column_name = :column_name')\
            .bindparams(table_name=self.args.table, column_name=column_name)
        result = self.connection.execute(query, {"table_name": self.args.table, "column_name": column_name}).scalar()

        if not result:
            return False, None

        data_type = result.lower()
        maskable_types = ['array', 'text', 'jsonb', 'character varying']
        is_maskable = data_type in maskable_types

        return is_maskable, data_type if is_maskable else None

    def mask_text_data(text_data):
        for pattern_name, pattern in patterns.items():
            replace_function = replace_functions.get(pattern_name, lambda x: x)
            text_data = pattern.sub(replace_function, text_data)

        return text_data

    def mask_json_data(json_data):
        masked_data = json_data.copy()
        for key, value in masked_data.items():
            if isinstance(value, str) and value.startswith('{'):
                masked_data[key] = MaskUtils.mask_json_data(json.loads(value))
            elif isinstance(value, list):
                masked_data[key] = [
                    MaskUtils.mask_json_data(line)
                    if (isinstance(line, dict) or (isinstance(line, str) and line.startswith('{')))
                    else MaskUtils.mask_text_data(line)
                    for line in value
                ]
            elif isinstance(value, dict) or (isinstance(value, str) and value.startswith('{')):
                masked_data[key] = MaskUtils.mask_json_data(value)
            elif isinstance(value, str):
                masked_data[key] = MaskUtils.mask_text_data(value)

        masked_json_data = json.dumps(masked_data)

        return masked_json_data

    def mask_character_varying_data(char_var_data):
        if isinstance(char_var_data, list):
            char_var_data = [
                MaskUtils.mask_json_data(item)
                if (isinstance(item, dict) or (isinstance(item, str) and item.startswith('{')))
                else MaskUtils.mask_text_data(item)
                for item in char_var_data
            ]
        return char_var_data

    def mask_with_regex(self):
        columns = self.args.columns if self.args.columns else self.get_table_columns()

        try:

            total_rows = self.connection.execute(text(f"SELECT COUNT(*) FROM {self.args.table}")).scalar()

            signal.signal(signal.SIGINT, MaskUtils.handler)

            for column in columns:
                maskable, data_type = self.is_column_maskable(column)
                if not maskable:
                    print(f"Skipping column '{column}' because its type is not maskable.")
                    continue

                for offset in range(0, total_rows, CHUNK_SIZE):
                    query = text(
                        f"SELECT id, {column} FROM {self.args.table} ORDER BY id LIMIT {CHUNK_SIZE} OFFSET {offset};"
                    )
                    id_and_column_data = self.connection.execute(query).fetchall()

                    for tuple_data in id_and_column_data:
                        row_id, old_value = tuple_data
                        if old_value is not None:
                            if data_type == 'character varying' or data_type == 'text':
                                old_value = MaskUtils.mask_text_data(old_value)
                            elif data_type == 'jsonb':
                                old_value = MaskUtils.mask_json_data(old_value)
                            elif data_type == 'array':
                                old_value = MaskUtils.mask_character_varying_data(old_value)

                            update_query = text(
                                f"UPDATE {self.args.table} SET {column} = :regenerated_value WHERE id = :row_id"
                            )
                            self.connection.execute(update_query, {"regenerated_value": old_value, "row_id": row_id})
                            self.connection.commit()
                    print(f"Updated {CHUNK_SIZE} rows in {self.args.table} for {column}, offset: {offset}")

            self.connection.close()
        except Exception as e:
            print("error : ", e)

    def mask_table_columns(self, CHUNK_SIZE=1000):
        total_rows = self.connection.execute(text(f"SELECT COUNT(*) FROM {self.args.table}")).scalar()

        signal.signal(signal.SIGINT, MaskUtils.handler)

        columns = self.args.columns if self.args.columns else self.get_table_columns()

        for column in columns:
            maskable, data_type = self.is_column_maskable(column)

            if not maskable:
                print(f"Skipping column '{column}' because its type is not maskable.")
                continue

            for offset in range(0, total_rows, CHUNK_SIZE):
                query = text(
                    f"SELECT id, {column} FROM {self.args.table} ORDER BY id LIMIT {CHUNK_SIZE} OFFSET {offset}; "
                )
                id_and_column_data = self.connection.execute(query).fetchall()

                for tuple_data in id_and_column_data:
                    row_id, old_value = tuple_data
                    if old_value is not None:
                        regenerated_value = MaskUtils.mask_data_type(old_value, data_type)

                        update_query = text(
                            f"UPDATE {self.args.table} SET {column} = :regenerated_value WHERE id = :row_id"
                        )

                        self.connection.execute(update_query, {"regenerated_value": regenerated_value, "row_id": row_id})
                self.connection.commit()
                print(f"Updated {CHUNK_SIZE} rows in {self.args.table} for {column}, offset: {offset}")
        self.connection.close()

    def mask_data_type(data, data_type):
        if data_type == 'jsonb':
            masked_data = json.dumps({"key": "masked_value"})
        elif data_type == 'array':
            masked_data = ['*' * len(str(item)) for item in data]
        else:
            masked_data = '*' * len(str(data))

        return masked_data


