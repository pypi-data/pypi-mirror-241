from application.core.parser_data import init_data_processing
from application.core.jobs.get_masked_or_deleted_db import delete_rows_in_chunks, mask_data_in_table, all_mask
from application.core.parser_data import get_table_columns


def main():
    command_line_args, conn = init_data_processing()
    if conn is not None:
        if command_line_args.action == 'delete':
            if command_line_args.table and command_line_args.percentage:
                confirm = input(f"{command_line_args.percentage}% of the {command_line_args.table} table will be "
                                f"deleted, do "
                                f"you confirm? (Y/N): ").lower()
                if confirm == 'y':
                    delete_rows_in_chunks(conn, command_line_args.table, command_line_args.percentage, chunk_size=500)
                else:
                    print("Operation canceled.")
            else:
                print("No table or percentage data to be deleted has been entered")
        elif command_line_args.action == 'mask':
            if command_line_args.table:
                if command_line_args.columns is not None:
                    confirm = input("The columns {} of the {} table will be masked, do you confirm? (Y/N): ".format(', '.join(command_line_args.columns), command_line_args.table)).lower()
                else:
                    confirm = input("All columns of the {} table will be masked, do you confirm? (Y/N): ".format(command_line_args.table)).lower()
                if confirm == 'y':
                    if not command_line_args.columns:
                        mask_data_in_table(conn, command_line_args.table,
                                           get_table_columns(command_line_args.table, conn))
                    else:
                        if command_line_args.mask_type != 'all':
                            mask_data_in_table(conn, command_line_args.table, command_line_args.columns)
                        else:
                            all_mask(conn, command_line_args.table, command_line_args.columns)
                else:
                    print("Operation canceled.")
            else:
                print("No table or columns data to be deleted has been entered")

        else:
            print("Invalid Action: ", command_line_args.action)
    else:
        print('Could not connect to database')


if __name__ == "__main__":
    main()
