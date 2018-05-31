from muddypy.muddydb import muddydb

class muddypy():
    def __init__(self, msg):
        print("I am now initialized:", msg)
        self.db = muddydb()
