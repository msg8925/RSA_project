import sqlite3

class DB_context_manager():

    # init method runs when object is created
    def __init__(self, DBname):
        self.DBname = DBname
        

    # enter method runs when an operation such as a write is performed
    def __enter__(self):
        self.conn = sqlite3.connect(self.DBname)
        self.c = self.conn.cursor()
    
        return self.c

    # exit method runs when an operation has finshed
    def __exit__(self, exc_type, exc_cal, traceback):
        self.conn.commit()
        self.conn.close()
  