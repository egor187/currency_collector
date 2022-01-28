import os

from sqlalchemy import create_engine, select, inspect
from sqlalchemy.orm import Session
from dotenv import load_dotenv, find_dotenv
from schema import Currency, CurrencyData, engine, session
from exc import DataNotFound

# load_dotenv(find_dotenv())
#
# engine = create_engine(os.getenv("DOCKER_SQLALCHEMY_DATABASE_URL"))
# # engine = create_engine(os.getenv("LOCAL_SQLALCHEMY_DATABASE_URL"))
# session = Session(engine)
# Base.metadata.create_all(engine)


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


def get_currency_id_by_code(currency_code: str):
    with session:
        currency_id = session.execute(
            select(Currency.id).where(Currency.code == currency_code)
        ).fetchone()
    if not currency_id:
        raise DataNotFound
    return currency_id[0]


def add_currency_data(currency_code: str, data: dict) -> None:
    with session:
        try:
            currency_id = get_currency_id_by_code(currency_code)
        except DataNotFound:
            print("No such currency code")
        else:
            for key in data.keys():
                obj = CurrencyData(currency_id=currency_id, date=key, value=data[key])
                session.add(obj)
        session.commit()


def _check_db():
    """Check is db has 'currency' table"""
    return inspect(engine).has_table("currency")
