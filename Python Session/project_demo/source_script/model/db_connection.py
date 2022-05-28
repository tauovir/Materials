from source_script.configuration.config import *

import sqlalchemy
import sqlite

from sqlalchemy.exc import SQLAlchemyError

class DBConnection:

    def __init__(self):
        self.conn = None

    def get_engine(self):
        try:
            #engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')
            connection_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            engine = sqlalchemy.create_engine(connection_url)
            return engine
        except SQLAlchemyError as e:
            print("Exception")
            raise (e)

    def get_connection(self):
        engine = self.get_engine()
        self.conn = engine.connect()
        return self.conn

    def close_connection(self):
        if self.conn:
            self.conn.close()


class SQLLiteConnection:

    def __init__(self):
        self.conn = None

    def get_engine(self):
        try:
            connection_url = r'sqlite:///C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\sqlite\in_house.db'
            engine = sqlalchemy.create_engine(connection_url)
            return engine
        except Exception as e:
            print("Exception")
            raise (e)

    def get_connection(self):
        engine = self.get_engine()
        self.conn = engine.connect()
        return self.conn

    def close_connection(self):
        if self.conn:
            self.conn.close()



if __name__ == "__main__":
    sql = "select * from users"
    obj = DBConnection()

    conn = obj.get_connection()
    data = conn.execute(sql)  # execute method to execute data
    user_data = []
    columns = data.keys()
    print("columns:",columns)
    for r in data:
        row_data = dict(zip(columns, r))
        user_data.append(row_data)
    print("==========")
    print(user_data)