import sqlite3
db = sqlite3.connect("database/stones.db")
print("Database Created")
db.close()