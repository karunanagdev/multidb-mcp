import sqlite3
import pandas as pd
from config import DATABASE_TYPE
from logger import logger

class Database:

    def __init__(self, db_path):
        if DATABASE_TYPE == "sqlite":
            self.conn = sqlite3.connect(db_path)

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
            cursor = self.conn.cursor()    
            cursor.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logger.error(str(e))

            raise

        return cursor.rowcount
    
    def close(self):
        self.conn.close()

    def get_connection(self):
        return self.conn
    
    def transaction(self):

        return self.conn