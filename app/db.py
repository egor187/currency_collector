import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv, find_dotenv
from app.schema import Base, Currency

load_dotenv(find_dotenv())

engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URL"))
session = Session(engine)
Base.metadata.create_all(engine)


def currencies_db_init(lst: list):
    with session:
        for obj in lst:
            session.add(obj)
        session.commit()