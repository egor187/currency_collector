import os

from sqlalchemy import create_engine, select, inspect
from sqlalchemy.orm import Session
from dotenv import load_dotenv, find_dotenv
from schema import Base, Currency
from exc import DataNotFound

load_dotenv(find_dotenv())

engine = create_engine(os.getenv("DOCKER_SQLALCHEMY_DATABASE_URL"))
# engine = create_engine(os.getenv("LOCAL_SQLALCHEMY_DATABASE_URL"))
session = Session(engine)
Base.metadata.create_all(engine)


def currencies_db_init(lst: list):
    with session:
        for obj in lst:
            session.add(obj)
        session.commit()


def get_currency_code_by_name(currency_name: str):
    """Map provided currency name to it code from db"""
    with session:
        currency_code = session.execute(
            select(Currency.code).where(Currency.name == currency_name)
        ).fetchone()
    if not currency_code:
        raise DataNotFound
    return currency_code[0]


def _check_db():
    """Check is db has 'currency' table"""
    if not inspect(engine).has_table("currency"):
        return True
    else:
        return False
