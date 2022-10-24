import psycopg2
from sqlalchemy import create_engine, MetaData
from utils.files import get_assets

config = get_assets('config')
DATABASE_URL = config['url']['database']

class DBConn:
    __instance = None
    connection = None
    error = None
    metadata = MetaData()
    engine = create_engine(DATABASE_URL)

    def __new__(cls):
        if DBConn.__instance is None:
            DBConn.__instance = object.__new__(cls)
        return DBConn.__instance

    def __init__(self):
        try:
            if self.connection is None:
                print('Connecting to the PostgreSQL database')
                self.connection = psycopg2.connect(DATABASE_URL,
                                                    connect_timeout=3)

                print('Connected to database')
            else:
                print("This singleton pattern, connection is ready")

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.error = error

    def close(self):
        if self.connection:
            try:
                self.connection.close()
                print('Database connection closed.')
            except Exception:
                pass
        self.connection = None

    def connect(self):
        self.close()
        self.__init__()

    def connected(self):
        return self.connection and self.connection.closed == 0

DB = DBConn()
