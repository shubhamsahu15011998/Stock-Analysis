import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from utility import get_exception_meta_details


class SQLSession:

    engine = None

    @classmethod
    def get_database_connection(cls, max_retries=int(os.environ.get("MAX_DB_RETRY", 5)), echo=False):
        if not cls.engine:
            for attempt in range(max_retries):
                try:
                    engine = create_engine(
                        os.environ.get("DB_URL"),
                        echo=echo,
                        pool_size=int(os.environ.get("SQL_DB_POOL_SIZE")), # pool_size=5 → Maintains 5 active connections.
                        max_overflow=int(os.environ.get("SQL_DB_MAX_OVERFLOW")) # max_overflow=10 → Allows 10 additional temporary connections if the pool is full.
                    )
                    engine.connect()
                    Base.metadata.create_all(engine)
                    cls.engine = engine
                except Exception as e:
                    if attempt < max_retries - 1:
                        print(f"Connection attempt {attempt + 1} failed. Retrying Now ...")
                    else:
                        raise Exception(f"Failed to connect to database after {max_retries} attempts: {get_exception_meta_details()}")
        return cls.engine

    @classmethod
    def get_session(cls):
        try:
            engine = cls.get_database_connection()
            session = sessionmaker(bind=engine)
            return session()
        except Exception as e:
            raise Exception(f"Failed in getting a session, Error Details {get_exception_meta_details()}")
