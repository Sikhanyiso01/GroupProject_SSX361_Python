import sqlite3

class Database:
   def __init__(self, db):
       self.conn = sqlite3.connect(db)
       self.cur = self.conn.cursor()
       self.cur.execute(
           "CREATE TABLE IF NOT EXISTS Book( BookID INTEGER AUTOINCREMENT PRIMARY KEY, title text, author text, ISBN text, genre text, Avaliability_Status text)")
       self.cur.execute(
           "CREATE TABLE IF NOT EXIST Member( title INTEGER PRIMARY KEY, Name text, MembershipID text, Contact text, MembershipType text CHECK(MembershipType IN ('regular', 'Premium') "
       )
       self.conn.commit()

   def fetch_book(self):
       self.cur.execute("SELECT * FROM Books")
       rows = self.cur.fetchall()
       return rows
   def insert_book(self, bookID,title, author , ISBN, genre, availability_status):
       self.cur.execute("INSERT INTO Book VALUES (NULL, ?, ?, ?, ?, ?)", (bookID, title, author, availability_status))
       self.conn.commit()


