#!/usr/bin/env python3

from driver import RemoteWBDriver, WBDriver
from parser import populate_db_with_currencies, parse_currency_html
from db import get_currency_code_by_name
from exc import DataNotFound


def main():
    # currency_code = sys.argv[1]  #TODO try to apply instead user input
    flag = True

    while flag:
        currency_name = input("Provide a currency name: ")

        try:
            currency_code = get_currency_code_by_name(currency_name=currency_name)
        except DataNotFound:
            print("No such currency founded")
        else:
            flag = False
            # currency_html = WBDriver(currency_code=currency_code).get_currency_html()
            currency_html = RemoteWBDriver(currency_code=currency_code).get_currency_html()
            currency_data = parse_currency_html(currency_html=currency_html)
            populate_db_with_currencies(currency_html=currency_html)


if __name__ == "__main__":
    main()
