#!/usr/bin/env python3

import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup

from driver import LocalWBDriver
from parser import parse_currency_html


def main():
    # currency_code = sys.argv[1]
    currency_code = "R01010"  # TODO fix hardcoded currency code
    currency_html = LocalWBDriver(currency_code=currency_code).get_currency_html()
    currency_data = parse_currency_html(currency_html=currency_html)


if __name__ == "__main__":
    main()
