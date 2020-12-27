import argparse
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from exercise_2.scripts.database_manager import ScientificCommunityDBManager


def _parse_user_args():
    """
    Parses the user arguments
    :returns: user arguments
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-d', '--database', help="the name of the database", required=True)
    arg_parser.add_argument('-pwd', '--password', help="password for the specified database user", required=True)
    arg_parser.add_argument('-u', '--user', nargs='?', default="postgres",
                            help="database user, defaults to postgres")
    arg_parser.add_argument('-i', '--ip', nargs='?', default="localhost",
                            help="connection ip, defaults to localhost")
    arg_parser.add_argument('-p', '--port', nargs='?', default="5432", help="connection port, defaults to 5432")
    return arg_parser.parse_args()


if __name__ == "__main__":
    args = _parse_user_args()
    db_manager = ScientificCommunityDBManager.create(database=args.database, password=args.password, user=args.user,
                                                     host=args.ip, port=args.port)
    db_manager.truncate_tables()
    db_manager.generate_and_insert_fake_data()
