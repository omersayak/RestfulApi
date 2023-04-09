from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser

config = ConfigParser()
config.read('app/settings.ini')

username = config.get('database', 'username')
password = config.get('database', 'password')
url = config.get('database','url')
database_name = config.get('database', 'database')


DATABASE_URL = f"postgresql://{username}:{password}@{url}/{database_name}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()