import sqlite3
import pandas as pd

conn = sqlite3.connect("data/maritime.db")

df = pd.read_sql(
    "SELECT * FROM vessels",
    conn
)

print(df.head())

print("\nColumns:")
print(df.columns)

print("\nInfo:")
print(df.info())

conn.close()