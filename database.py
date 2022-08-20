from sqlalchemy import  create_engine
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.ext.declarative import  declarative_base

# create database url
SQLALCHEMY_DATABASE_URL = "slite:///./todos.db"

# create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
)

# session -- database local session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()