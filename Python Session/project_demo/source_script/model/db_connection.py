from source_script.configuration.config import *
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

class DBConnection:

    def __init__(self):
        self.conn = None

    def get_engine(self):
        try:
            #engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')
            if IS_POSTGRES_DB:
                connection_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            else:
                connection_url = SQLITE_DB_PATH
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




if __name__ == "__main__":
    pass