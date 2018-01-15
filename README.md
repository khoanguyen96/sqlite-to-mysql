sqlite-to-mysql
===============

Script to convert and add SQLite3 database into a MySQL/MariaDB database

## Description

This script is used to convert a SQLite3 .db file into a multiple SQL files based on their tablenames.  It was forked from [sqlite-to-mysql](https://github.com/vwbusguy/sqlite-to-mysql).  I've mostly rewrote the original using Python classes and added another class that handled
multiple writing SQL files, as importing one huge SQL file can (if not mostly) fail.


## Dependencies

- Sqlite 3 `sqlite3`
- Python 2.7 `python`

## Usage

Included are the `convert.sh` and `dump.sh` script files to use. You can change these script files to suit your needs.

Common Steps:
1) Dump SQLite file schema and data into two files.
2) Remove schema and retain only the data.
3) Run Python script to convert into MySQL syntax.

(Similar to `convert.sh`)

```bash
# Dump SQLite schema
sqlite3 /path/to/sqlite/file.sqlite .schema > data/schema.sql

# Dump SQLite data completely
sqlite3 /path/to/sqlite/file.sqlite .dump > data/dump.sql

# Remove Schema from Dump file
grep -vx -f data/schema.sql data/dump.sql > data.sql

# Run this Python script specifying the dumped sql file and output directory

./sqlite3_to_mysql.py data/data.sql data/

```

That's it!  Import the *.sql files into your MySQL database! Assuming you don't need to import the schema for the MySQL database as well.

## Notes

There isn't any forseeable reason for this not to work on Windows using sqlite.exe and mysql.exe, etc.  I have not testing this.

As always, use your common sense and backup your data before attempting this.  If you pick a database name that already exists in your mysql instance, expect the data to be overwritten.

Enjoy!
