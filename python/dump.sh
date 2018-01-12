#!/bin/bash

db_sqlite=$1
echo $1

# get data only, no schema here bois...
sqlite3 ${db_sqlite} .schema > data/tmpschema.sql
sleep 1

sqlite3 ${db_sqlite} .dump > data/tmpdump.sql
sleep 1

grep -vx -f data/tmpschema.sql data/tmpdump.sql > data.sql

# convert data.sql to mysql format
# using https://github.com/vwbusguy/sqlite-to-mysql

cat data/tmpdump.sql | ./sqlite3-to-mysql.py > data/mysqldata.sql

# partition to multiple .sql files
./partition-sql.py data/mysqldata.sql data

# remove all the files
rm -f data/tmpschema.sql data/tmpdump.sql data/mysqldata.sql