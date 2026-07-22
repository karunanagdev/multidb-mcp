import sqlite3
import pandas as pd
from pathlib import Path


class Database:

    def __init__(self):

        base_path = Path(__file__).resolve().parents[2]

        db_path = base_path / "data" / "maritime.db"

        self.connection = sqlite3.connect(db_path)


    def query(self, sql):

        return pd.read_sql_query(
            sql,
            self.connection
        )