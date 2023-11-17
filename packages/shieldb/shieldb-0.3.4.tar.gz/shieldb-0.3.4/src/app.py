from application.core.enums import Actions
from application.core.mask_utils import MaskUtils
from application.core.utils import Utils


def main():
    args = Utils.read_user_args()
    connection = Utils.connect_db()

    if connection is None:
        print("Could not connection ect to database")
        return

    if args.action not in [Actions.DELETE.value, Actions.MASK.value]:
        print("Invalid Action: ", args.action)
        return

    mask_utils = MaskUtils(connection, args)

    if args.action == Actions.DELETE.value:
        confirm = input(f"{args.percentage}% of the {args.table} table will be "
                        f"deleted, do "
                        f"you confirm? (Y/N): ").lower()
        if confirm == 'y':
            mask_utils.delete_rows_in_chunks()
        else:
            print("Operation canceled.")

    elif args.action == Actions.MASK.value:
        if (not args.table) and (not args.columns):
            print("No table or columns data to be deleted has been entered")
            return

        confirm = input(
            "All columns of the {} table will be masked, do you confirm? (Y/N): ".format(args.table)).lower()
        if confirm == 'y':
            if args.mask_type == 'all':
                mask_utils.mask_table_columns()
            else:
                mask_utils.mask_with_regex()
        else:
            print("Operation canceled.")


if __name__ == "__main__":
    main()
