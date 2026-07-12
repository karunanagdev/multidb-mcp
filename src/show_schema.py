import sqlite3

conn = sqlite3.connect("data/maritime.db")

cursor = conn.cursor()

tables = ["ports", "vessels", "voyages", "cargo"]

for table in tables:
    print(f"\n===== {table.upper()} =====")

    cursor.execute(f"PRAGMA table_info({table})")

    columns = cursor.fetchall()

    for col in columns:
        print(col)

conn.close()