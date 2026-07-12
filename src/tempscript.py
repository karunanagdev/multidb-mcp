from database import Database
from config import DATABASE_PATH

db = Database(DATABASE_PATH)

result = db.query("PRAGMA foreign_keys;")

print(result)
print(db.query("PRAGMA foreign_key_list(voyages);"))
print(db.query("PRAGMA foreign_key_list(cargo);"))