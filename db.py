import sqlite3

class Database:
   def __init__(self, db):
       self.conn = sqlite3.connect(db)
       self.cur = self.conn.cursor()
       self.cur.execute(
           "CREATE TABLE IF NOT EXISTS Book( title INTEGER PRIMARY KEY, author text, ISBN text, genre text, Avaliability_Status text)")
       self.cur.execute(
           "CREATE TABLE IF NOT EXIST MembershipID AUTOINCREMENT INTEGER PRIMARY KEY, Name text, Contact text, MembershipType text CHECK(MembershipType IN ('regular', 'Premium') "
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

   def select_members(self):
       self.cur.execute("SELECT * FROM Members")
       rows = self.cur.fetchall()
       return rows

   def insert_members(self, membershipid, name, contact, membershiptype):
       self.cur.execute("INSERT INTO Members VALUES (NULL, ?, ?, ?)", (membershipid, name, contact, membershiptype))
       self.conn.commit()

   def update_members(self, membershipid, name, contact, membershiptype):
       self.cur.execute(
           "UPDATE Members SET MembershipID=?, Name=?, Contact=?, MembershipType=?, WHERE MembershipID=? )",
           (membershipid, name, contact, membershiptype))
       self.conn.commit()

   def delete_members(self, membershipid):
       self.cur.execute("DELETE FROM Members VALUES (MembershipID=?)", (membershipid,))
       self.conn.commit()

def __del__(self):
    self.conn.close()
db = Database("LibraryDB.db")