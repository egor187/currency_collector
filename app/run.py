#!/usr/bin/env python3
import sys

from driver import RemoteWBDriver
from parser import populate_db_with_currencies, parse_currency_html
from db import get_currency_code_by_name, add_currency_data
from exc import DataNotFound


FIRST_SEARCH_YEAR = "1992"


def main():
    flag = True

    while flag:
        currency_name = sys.argv[1]
        # currency_name = input("Provide a currency name: ")
        populate_db_with_currencies()
        try:
            currency_code = get_currency_code_by_name(currency_name=currency_name)
        except DataNotFound:
            print("No such currency founded")
        else:
            flag = False
            # currency_html = WBDriver(
            # currency_code=currency_code, first_year_search=FIRST_SEARCH_YEAR
            # ).get_currency_html()
            currency_html = RemoteWBDriver(
                currency_code=currency_code, first_year_search=FIRST_SEARCH_YEAR
            ).get_currency_html()
            currency_data = parse_currency_html(currency_html=currency_html)
            populate_db_with_currencies(currency_html=currency_html)
            add_currency_data(currency_code, currency_data)


if __name__ == "__main__":
    main()
