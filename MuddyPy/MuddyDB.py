import sqlite3

class MuddyDB():
    def __init__(self, dbfile):
        self.dbfile = dbfile
        try:
            self._conn = sqlite3.connect(self.dbfile)
        except:
            raise RuntimeError("error opening DB "+self.dbfile)
