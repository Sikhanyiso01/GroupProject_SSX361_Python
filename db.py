import sqlite3

class Database:
   def __init__(self, db):
       self.conn = sqlite3.connect(db)
       self.cur = self.conn.cursor()
       self.cur.execute(
           "CREATE TABLE IF NOT EXISTS Book( title text PRIMARY KEY, author text, ISBN text, genre text, Avaliability_Status text)")
       self.cur.execute(
           "CREATE TABLE IF NOT EXISTS Members (membershipid  INTEGER PRIMARY KEY AUTOINCREMENT, name text, Contact text, membershiptype text)"
       )

       self.conn.commit()

   def fetch_book(self):
       self.cur.execute("SELECT * FROM Book")
       rows = self.cur.fetchall()
       return rows

   def insert_book(self, title, author, ISBN, genre, availability_status):
       self.cur.execute("INSERT INTO Book (title, author, ISBN, genre, Avaliability_Status) VALUES (?, ?, ?, ?, ?)",
                        (title, author, ISBN, genre, availability_status))
       self.conn.commit()

   def delete_book(self, title):
       self.cur.execute("DELETE FROM Book WHERE title=?", (title,))
       self.conn.commit()

   def  update_book(self,title, author , ISBN, genre, availability_status):
       self.cur.execute("UPDATE Book SET title=?, author=?, ISBN=?, genre=? WHERE title=? )" , ( author,ISBN, genre, availability_status, title))
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
           "UPDATE Members SET MembershipID=?, Name=?, Contact=?, MembershipType=?, WHERE MembershipID=! )",
           (membershipid, name, contact, membershiptype))
       self.conn.commit()



   def delete_members(self, membershipid):
       self.cur.execute("DELETE FROM Members VALUES (MembershipID?)", (membershipid,))
       self.conn.commit()



   def __del__(self):
       self.conn.close()

if __name__ == "__main__":
    db = Database("LibraryDB.db")
    print("Database and tables created successfully."



