#! /usr/bin/env python

import argparse
import os

from sqlite2sql import Sqlite2Sql

def perfect_directory(path):
    absolute_path = os.path.abspath(path)

    if not os.path.exists(absolute_path):
        msg = "%s does not exist or is not a valid directory" % path
        raise argparse.ArgumentTypeError(msg)
    else:
        return absolute_path

def main():
    # cmd parser
    parser = argparse.ArgumentParser()
    parser.add_argument('sqlite',
                        type=argparse.FileType('r'), metavar="F",
                        help="sqlite file to convert to sql")

    parser.add_argument('directory',
                        type=perfect_directory,
                        metavar="D",
                        help="directory to write sql files to")

    args = parser.parse_args()

    # convert!
    sqlite2sql = Sqlite2Sql(args.sqlite)
    sqlite2sql.convert(args.directory)

if __name__ == "__main__":
    main()
