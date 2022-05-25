from source_script.configuration.config import *
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError


class DBConnection:

    def __init__(self):
        self.conn = None

    def get_engine(self):
        try:
            connection_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            engine = sqlalchemy.create_engine(connection_url)
            return engine
        except SQLAlchemyError as e:
            print("Exception")
            raise (e)

    def get_connection(self, array_size=1000):
        engine = self.get_engine()
        self.conn = engine.connect()
        return self.conn

    def close_connection(self):
        if self.conn:
            self.conn.close()
