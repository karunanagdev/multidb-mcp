import sqlite3
import pandas as pd
from config import DATABASE_TYPE
from logger import logger

class Database:

    def __init__(self, db_path):
        if DATABASE_TYPE == "sqlite":
            self.conn = sqlite3.connect(db_path)
            self.conn.execute("PRAGMA foreign_keys = ON")
            self.cursor = self.conn.cursor()
            #self.conn = sqlite3.connect(db_path)

        #elif DATABASE_TYPE == "postgresql":
            #connect using psycopg
                

    #def query(self, sql):
     #   return pd.read_sql(sql, self.conn)
    
    def query(self, sql, params=None):
        logger.info("Executing SELECT")
        logger.info(sql)
        logger.info(params)
        try:
            if params is None:
                params = ()
        
            return pd.read_sql(
                sql,
                self.conn,
                params=params)
        except Exception as e:
            logger.error(str(e))
            raise        

    def execute(self, sql, params=None):
        logger.info("Executing INSERT/UPDATE/DELETE")
        logger.info(sql)
        logger.info(params)
        if params is None:
            params = ()
        try:
            self.cursor.execute(sql, params)
            self.commit()
        except Exception as e:
            self.rollback()
            logger.error(str(e))

            raise

        return self.cursor.rowcount
    
    def close(self):
        self.conn.close()

    def get_connection(self):
        return self.conn
    
    def begin(self):

        logger.info("BEGIN TRANSACTION")

    def commit(self):

        logger.info("COMMIT")

        self.conn.commit()
    
    def rollback(self):

        logger.info("ROLLBACK")

        self.conn.rollback()

    def transaction(self):

        return self.conn
    
    def insert(self, sql, params=None):

        return self.execute(sql, params)
    
    def update(self, sql, params=None):

        return self.execute(sql, params)
    
    def delete(self, sql, params=None):

        return self.execute(sql, params)
    
    def execute_transaction(self, operations):

        try:

            self.begin()

            results = []

            for sql, params in operations:

                self.cursor.execute(sql, params)
                results.append(self.cursor.lastrowid)

            self.commit()

            return results

        except Exception:

            self.rollback()

            raise

    def execute_sql(self, sql, params=None):

        if params is None:
            params = ()

        self.cursor.execute(sql, params)

        return self.cursor