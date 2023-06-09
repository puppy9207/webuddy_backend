import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB = os.environ.get("POSTGRES_DB")
SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@webuddy_database/{DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = None
    try:
        print(f"************{USER}************")
        db = SessionLocal()
        yield db
    finally:
        db.close()
