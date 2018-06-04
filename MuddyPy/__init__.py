from MuddyPy.MuddyDB import MuddyDB

class MuddyPy():
    def __init__(self, **kwargs):
        print("I am now initialized:", kwargs['msg'])
        self.db = MuddyDB(kwargs['db'])
