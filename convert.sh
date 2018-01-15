#!/bin/sh

db_sqlite="$1"

if [ ! -z "$db_sqlite" ]; then
  echo $db_sqlite

  # get data only, no schema here bois...
  sqlite3 ${db_sqlite} .schema > data/tmpschema.sql
  sleep 1

  sqlite3 ${db_sqlite} .dump > data/tmpdump.sql
  sleep 1

  grep -vx -f data/tmpschema.sql data/tmpdump.sql > data/data.sql

  # convert data.sql to mysql format
  # partition to multiple .sql files
  ./sqlite3_to_mysql.py data/data.sql data

  # remove all the files
  # rm -f data/tmpschema.sql data/tmpdump.sql data/data.sql
else
  echo "No .sqlite file given!"
fi