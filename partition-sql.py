#! /usr/bin/env python
import sys, re, fileinput

# parse file
file = sys.argv[1]
dirr = sys.argv[2]

lines = (l for l in fileinput.input(file))
sections = dict()

for line in lines:
  tableNameRe = re.search('INSERT INTO (\w*) VALUES', line, re.IGNORECASE)

  if (tableNameRe):
    name = tableNameRe.group(1).strip()

    if name not in sections:
      print name
      sections[name] = list()

    sections[name].append(line)

print "Writing files to " + dirr

for key, values in sections.iteritems():
  writeFile = open(dirr + "/" + key + ".sql", "w")

  for line in values:
    writeFile.write(line)

  writeFile.close()

print "Done writing files..."