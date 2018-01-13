import tempfile
from partition import Partition

class Sqlite2Sql:
    def __init__(self, sqlite):
        self.source = sqlite
        self.lines = list()

    def replace_match_allcase(self, line, src, dest):
        line = line.replace(src, dest)
        line = line.replace(src.lower(), dest)

        return line

    def replace_backticks_except_in_string(self, line, in_string):
        new_line = ''

        for char in line:
            if not in_string:
                if char == "'":
                    in_string = True
                elif char == "\"":
                    new_line = new_line + '`'
                    continue
            elif char == "'":
                in_string = False

        return new_line, in_string

    def replace(self, line):
        IGNOREDPREFIXES = [
            'PRAGMA',
            'BEGIN TRANSACTION;',
            'COMMIT;',
            'DELETE FROM sqlite_sequence;',
            'INSERT INTO "sqlite_sequence"',
        ]

        REPLACEMAP = {
            "INTEGER PRIMARY KEY": "INTEGER AUTO_INCREMENT PRIMARY KEY",
            "AUTOINCREMENT": "AUTO_INCREMENT",
            "DEFAULT 't'": "DEFAULT '1'",
            "DEFAULT 'f'": "DEFAULT '0'",
            ",'t'": ",'1'",
            ",'f'": ",'0'",
        }

        if any(line.startswith(prefix) for prefix in IGNOREDPREFIXES):
            return

        for (src, dest) in REPLACEMAP.items():
            line = self.replace_match_allcase(line, src, dest)

        return line

    def preprocess(self):
        for line in self.source:
            encoded_line = line.encode('string_escape')
            self.lines.append(encoded_line)

    def parse(self):
        in_string = False
        for line in self.lines:
            if not in_string:
                line = self.replace(line)
                if line is None:
                    continue
            line, in_string = self.replace_backticks_except_in_string(line, in_string)

            yield line

    def read(self):
        self.preprocess()
        lines = (l for l in self.parse())

        tempf = tempfile.TemporaryFile()
        for line in lines:
            tempf.write(line)

        return tempf

    def convert(self, out):
        data = self.read()

        partitioner = Partition(data, out)
        partitioner.process()
