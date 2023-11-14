import json
import re
from sqlalchemy import text


def delete_rows_in_chunks(connection, table_name, percentage, chunk_size=1000):
    try:
        if not 0 <= percentage <= 100:
            print("Error: Percentage should be between 0 and 100.")
            return

        with connection.begin():
            total_rows = connection.execute(text(f'SELECT COUNT(*) FROM {table_name}')).scalar()
            rows_to_delete = int(total_rows * (percentage / 100))

            if rows_to_delete > 0:
                chunks = (rows_to_delete + chunk_size - 1) // chunk_size  # Calculate the number of chunks

                for chunk in range(chunks):
                    offset = chunk * chunk_size
                    limit = min(chunk_size, rows_to_delete - offset)

                    delete_query = text(
                        f'DELETE FROM {table_name} WHERE ctid IN (SELECT ctid FROM {table_name} ORDER BY RANDOM() OFFSET :offset LIMIT :limit)'
                    ).bindparams(offset=offset, limit=limit)
                    connection.execute(delete_query)

                print(f"{percentage}% of data deleted from the {table_name} table.")
            else:
                print(f"No rows to delete from the {table_name} table.")
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()


def replace_email(match):
    email = match.group(0)
    if len(email) > 2:
        parts = email.split("@")
        username = parts[0]
        new_email = email[0] + '*' * (len(username) - 2) + username[-1] + '@' + parts[1]
        return new_email
    else:
        return email


def replace_phone_number(match):
    phone = match.group(0)
    response = phone[:-4] + '****'
    return response


def replace_url(match):
    response = 'https://*****.com/***'
    return response


def replace_credit_card_number(match):
    credit_card_number = match.group(0)
    response = credit_card_number[:4] + '*' * (len(credit_card_number) - 4)
    return response


def replace_password(match):
    username = match.group(1)
    if len(match.group(2)) > 5:
        response = f"{username}******"
    else:
        response = f"{username}{match.group(2)}"
    return response


def mask_text_data(text_data, patterns, replace_functions):
    if isinstance(text_data, str):
        for pattern_name, pattern in patterns.items():
            replace_function = replace_functions.get(pattern_name, lambda x: x)
            text_data = pattern.sub(replace_function, text_data)
    elif isinstance(text_data, dict):
        for key, value in text_data.items():
            text_data[key] = mask_text_data(value, patterns, replace_functions)
    elif isinstance(text_data, list):
        text_data = [mask_text_data(item, patterns, replace_functions) for item in text_data]
    return text_data


def mask_json_data(json_data, patterns, replace_functions):
    data_dict = json_data

    for key, value in data_dict.items():
        if isinstance(value, str) and value[0] != '{':
            data_dict[key] = mask_text_data(value, patterns, replace_functions)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict) or (isinstance(item, str) and item[0] == '{'):
                    data_dict[key] = mask_json_data(json.loads(item), patterns, replace_functions)
                elif isinstance(item, str):
                    data_dict[key] = mask_text_data(item, patterns, replace_functions)
                elif isinstance(item, list):
                    data_dict[key] = [mask_text_data(line, patterns, replace_functions) for line in item]

        elif isinstance(value, dict) or (isinstance(value, str) and value[0] == '{'):
            if isinstance(value, str):
                value = json.loads(value)
            data_dict[key] = mask_json_data(value, patterns, replace_functions)

    masked_json_data = json.dumps(data_dict)

    return masked_json_data


def mask_character_varying_data(char_var_data, patterns, replace_functions):
    if isinstance(char_var_data, str):
        for pattern_name, pattern in patterns.items():
            replace_function = replace_functions.get(pattern_name, lambda x: x)
            char_var_data = pattern.sub(replace_function, char_var_data)
    elif isinstance(char_var_data, list):
        char_var_data = [mask_character_varying_data(item, patterns, replace_functions) for item in char_var_data]
    return char_var_data


def mask_data_in_table(connection, table_name, columns, chunk_size=100):
    try:
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

        replace_functions = {
            'email': replace_email,
            'phone': replace_phone_number,
            'tc': replace_phone_number,
            'credit_card': replace_credit_card_number,
            'password': replace_password,
            'url': replace_url,
        }

        total_rows = connection.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar()

        for column in columns:
            for offset in range(0, total_rows, chunk_size):
                query = text(
                    f"SELECT id, {column} FROM {table_name} ORDER BY id DESC LIMIT {chunk_size} OFFSET {offset};"
                )
                id_and_column_data = connection.execute(query).fetchall()

                for tuple_data in id_and_column_data:
                    row_id, old_value = tuple_data
                    if old_value is not None:
                        if isinstance(old_value, str):
                            old_value = mask_text_data(old_value, patterns, replace_functions)
                        elif isinstance(old_value, dict):
                            old_value = mask_json_data(old_value, patterns, replace_functions)
                        elif isinstance(old_value, list):
                            old_value = mask_character_varying_data(old_value, patterns, replace_functions)

                        update_query = text(
                            f"UPDATE {table_name} SET {column} = :regenerated_value WHERE id = :row_id"
                        )
                        connection.execute(update_query, {"regenerated_value": old_value, "row_id": row_id})
                        connection.commit()
                print(f"Updated {chunk_size} rows in {table_name} for {column}, offset: {offset}")

        connection.close()
    except Exception as e:
        print(f"Error: {e}")


def all_mask(connection, table_name, columns, chunk_size=100):
    total_rows = connection.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar()

    for column in columns:
        for offset in range(0, total_rows, chunk_size):
            query = text(
                f"SELECT id, LENGTH({column}) as char_count FROM {table_name} ORDER BY id LIMIT {chunk_size} OFFSET {offset}; "
            )
            id_and_column_data = connection.execute(query).fetchall()

            for tuple_data in id_and_column_data:
                row_id, old_value = tuple_data

                update_query = text(
                    f"UPDATE {table_name} SET {column} = :regenerated_value WHERE id = :row_id"
                )
                old_value = old_value * "*"
                connection.execute(update_query, {"regenerated_value": old_value, "row_id": row_id})
            connection.commit()
            print(f"Updated {chunk_size} rows in {table_name} for {column}, offset: {offset}")

    connection.close()
