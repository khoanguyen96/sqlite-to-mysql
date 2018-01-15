sqlite-to-mysql
===============

Script to convert and add sqlite3 database into a mysql/mariadb database

## Description

This script is used to convert a sqlite3 .db file into a running mysql/mariadb 5.x+ instance.  It was adapted from the code posted at http://www.redmine.org/boards/2/topics/12793?r=24999 .  I've mostly simply altered it to make the effort of use minimal.

The script works as a layer between sqlite and mysql to format the sqlite dump, create a new user and database in mysql, and restore all the tables and data in one shell line.

## Dependencies
Sqlite 3 `sqlite3`

Python 2.7 `python`

## Usage

Included are the `convert.sh` and `dump.sh` script files to use. You can change these script files to suit your needs.

Common Steps:
1) Dump SQLite file schema and data into two files.
2) Remove schema and retain only the data.
3) Run Python script to convert into MySQL syntax.

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
