import sqlite3

class Database:
   def __init__(self, db):
       self.conn = sqlite3.connect(db)
       self.cur = self.conn.cursor()
       self.cur.execute(
           "CREATE TABLE IF NOT EXISTS Book( title INTEGER PRIMARY KEY, author text, ISBN text, genre text, Avaliability_Status text)")
       self.cur.execute(
           "CREATE TABLE IF NOT EXIST Members( MembershipID INTEGER PRIMARY KEY, Name text, Contact text, MembershipType text")
       self.conn.commit()

def select_members(self):
    self.cur.execute("SELECT * FROM Members")
    self.conn.commit()

def insert_members(self, MembershipID, Name, Contact, MembershipType):
    self.cur.execute("INSERT INTO Members VALUES (?, ?, ?, ?)", (MembershipID, Name, Contact, MembershipType))
    self.conn.commit()

def update_members(self, MembershipID, Name, Contact, MembershipType):
    self.cur.execute("UPDATE Members VALUES (?, ?, ?, ?,)", (MembershipID, Name, Contact, MembershipType))
    self.conn.commit()

def delete_members(self, MembershipID, Name, Contact, MembershipType):
    self.cur.execute("DELETE FROM Members VALUES (?, ?, ?, ?,)", (MembershipID, Name, Contact, MembershipType))
    self.conn.commit()
