
from db import Database
import sqlite3

db = Database("LibraryDB.db")


book = db.fetch_book()
for books in book:
    print(books)

