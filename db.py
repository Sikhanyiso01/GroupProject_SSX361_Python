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
       self.cur.execute("INSERT INTO Book VALUES (NULL, ?, ?, ?, ?, ?)", (bookID, title, author, ISBN,genre, availability_status))
       self.conn.commit()

   def delete_book(self, bookID):
       self.cur.execute("DELETE FROM Book WHERE bookID=?", (bookID,))
       self.conn.commit()

   def  update_book(self,  bookID,title, author , ISBN, genre, availability_status):
       self.cur.execute("UPDATE Book SET title=?, author=?, ISBN=?, genre=? WHERE id=?)" , ( title, author,ISBN, genre, availability_status, bookID))
       self.conn.commit()

   def __del__(self):
       self.conn.close()
db = Database("LibraryDB.db")



