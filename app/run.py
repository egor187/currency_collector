#!/usr/bin/env python3

from driver import RemoteWBDriver, WBDriver
from parser import get_currency_mapper


def main():
    # currency_code = sys.argv[1]
    currency_code = "R01010"  # TODO fix hardcoded currency code
    # currency_html = WBDriver(currency_code=currency_code).get_currency_html()
    currency_html = RemoteWBDriver(currency_code=currency_code).get_currency_html()
    # currency_data = parse_currency_html(currency_html=currency_html)
    currency_list = get_currency_mapper(currency_html=currency_html)


if __name__ == "__main__":
    main()
