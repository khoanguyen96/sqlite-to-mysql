class Sqlite2Sql:
    def __init__(self, sqlite):
        self.source = sqlite

    def replace_match_allcase(line, src, dest):
        line = line.replace(src, dest)
        line = line.replace(src.lower(), dest)

        return line

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