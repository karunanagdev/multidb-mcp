from database import Database
from config import DATABASE_PATH

db = Database(DATABASE_PATH)

result = db.query("PRAGMA foreign_keys;")

print(result)