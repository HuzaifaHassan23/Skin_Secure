from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
load_dotenv()
from sqlalchemy import create_engine

DB_PASSWORD = os.getenv("DB_PASSWORD")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:{DB_PASSWORD}@localhost/skin_secure"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to inject the database session into our routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()