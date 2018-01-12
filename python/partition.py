import re, fileinput

class Partition:
    def __init__(self, sqlFile, outDir):
        self.sections = dict()
        self.file = fileinput.input(sqlFile)
        self.dir = outDir

    def read(self):
        for line in self.file:
            table_regex = re.search('INSERT INTO (\w*) VALUES', line, re.IGNORECASE)

            if table_regex:
                name = table_regex.group(1).strip()

                if name not in self.sections:
                    self.sections[name] = list()
                    print name
                self.sections[name].append(line)

    def write(self):
        for key, values in self.sections.iteritems():
            write_file = open(self.dir + "/" + key + ".sql", "w")

            for line in values:
                write_file.write(line)

            write_file.close()
