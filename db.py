import sqlite3

class Database:
   def __init__(self, db):
       self.conn = sqlite3.connect(db)
       self.cur = self.conn.cursor()
       self.cur.execute(
           "CREATE TABLE IF NOT EXISTS Book( title INTEGER PRIMARY KEY, author text, ISBN text, genre text, Avaliability_Status text)")
       self.conn.commit()
