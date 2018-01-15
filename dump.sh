#!/bin/sh

db_sqlite=$1

echo "Dumping $db_sqlite..."

# get data only, no schema here bois...
sqlite3 ${db_sqlite} .schema > data/tmpschema.sql
sleep 1

sqlite3 ${db_sqlite} .dump > data/tmpdump.sql
sleep 1

echo "Files dumped..."
