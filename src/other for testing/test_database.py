from database import Database

db = Database("data/maritime.db")

df = db.query(
    #"SELECT * FROM vessels LIMIT 10"
    """
    SELECT * FROM voyages;

"""
)

print(df)

db.close()