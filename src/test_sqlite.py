import sqlite3
import os

print("Current Directory:", os.getcwd())

#conn = sqlite3.connect("maritime.db")
conn = sqlite3.connect("data/maritime.db")

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = cursor.fetchall()

print("Tables:")
for table in tables:
    print(table)

conn.close()