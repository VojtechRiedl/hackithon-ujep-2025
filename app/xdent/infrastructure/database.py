

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.xdent.core.settings import settings

from sqlalchemy.orm import Session

from typing import Generator

class Database():
    def __init__(self):
        
        self.engine = create_engine(
            settings.database.url,
            connect_args={"check_same_thread": False},
            pool_pre_ping=True,
        )  # check_same_thread=False is only for SQLite
        
        self.session_local = sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
        )

        self.base = declarative_base()

    @property
    def Base(self):
        return self.base
    
    @property
    def session(self):
        return self.session_local()

    def get_db(self) -> Generator[Session, None, None]:
        db = self.session_local()
        try:
            yield db
        finally:
            db.close()

    def create_all(self):
        print("creating")
        self.base.metadata.create_all(bind=self.engine)
    

database = Database()
