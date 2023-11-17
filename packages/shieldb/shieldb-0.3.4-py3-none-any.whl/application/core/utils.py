import argparse
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


class Utils:
    @staticmethod
    def read_user_args():
        parser = argparse.ArgumentParser(prog='shieldb', description='Script for deleting or masking data from '
                                                                     'a database\n '
                                                                     'Before running the src, make sure to '
                                                                     'set the database '
                                                                     'to work with. '
                                                                     'You can set the database by defining the '
                                                                     'SQLALCHEMY_DATABASE_URI variable.\n '
                                                                     'Usage examples:\n'
                                                                     'SQLALCHEMY_DATABASE_URI=""'
                                                                     '%(prog)  --action delete --table my_table '
                                                                     '--percentage 20\n '
                                                                     '%(prog)  --action mask --table my_table '
                                                                     '--columns column1 '
                                                                     'column2')
        parser.add_argument('--action', choices=['delete', 'mask'], help='Operation to be performed')
        parser.add_argument('--table', help='Name of the table from which data will be deleted or masked')
        parser.add_argument('--percentage', type=float, default=0,
                            help='Percentage of data to be deleted (default: 0), PERCENTAGE SHOULD BE BETWEEN 0 AND 100.')
        parser.add_argument('--columns', nargs='+', default=[],
                            help='The columns to be masked will be entered with spaces. If columns are not entered, '
                                 'the entire table is masked.')
        parser.add_argument('--mask_type', help='Name of the table from which data will be deleted or masked')

        command_line_args = parser.parse_args()
        return command_line_args

    @staticmethod
    def connect_db():
        try:
            db_url = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:12345@localhost:5433/backup_dump')
            engine = create_engine(db_url)
            conn = engine.connect()
            return conn
        except SQLAlchemyError as e:
            return None
