from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import keys

# create database url
SQLALCHEMY_DATABASE_URL = f"postgresql://{keys.username}:{keys.password}@localhost/{keys.database}"

# create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# session -- database local session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
