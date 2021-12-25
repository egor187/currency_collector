from datetime import datetime

from bs4 import BeautifulSoup

from schema import Currency
from db import currencies_db_init, _check_db


def parse_currency_html(currency_html: str) -> dict:
    data_ = dict()

    currency_table = BeautifulSoup(currency_html, "html.parser").find("table", class_="data").find("tbody")
    currency_table_rows = currency_table.find_all("tr")
    for row in currency_table_rows:
        cols = row.find_all("td")
        cols = [elem.text.strip() for elem in cols]
        try:
            date_ = datetime.strptime(cols[0], "%d.%m.%Y")
            data_[date_] = float(cols[-1].replace(",", "."))
        except (IndexError, ValueError):
            pass
    return data_


def populate_db_with_currencies(currency_html: str) -> None:
    is_db_exist = _check_db()

    if not is_db_exist:
        currencies = list()

        currency_list = BeautifulSoup(
            currency_html,
            "html.parser"
        ).find(
            "select",
            id="UniDbQuery_VAL_NM_RQ"
        ).find_all("option")
        res = [{tag['value']: tag.text.strip()} for tag in currency_list]

        for elem in res:
            code = list(elem.keys())[0]
            name = list(elem.values())[0]
            currency = Currency(name=name, code=code)
            currencies.append(currency)

        currencies_db_init(currencies)
