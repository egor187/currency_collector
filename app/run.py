#!/usr/bin/env python3

from datetime import datetime
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup

from driver import Driver


def main():
    driver = Driver().get_local_driver()
    data_ = dict()

    # currency = sys.argv[1]
    currency_code = "R01010"

    driver.get("https://cbr.ru/currency_base/dynamics/")
    currency_selector = driver.find_element(By.ID, "UniDbQuery_VAL_NM_RQ")
    select_obj = Select(currency_selector)
    select_obj.select_by_value(currency_code)
    driver.find_element(By.ID, "UniDbQuery_searchbutton").click()
    html = driver.page_source

    currency_table = BeautifulSoup(html, "html.parser").find("table", class_="data").find("tbody")
    currency_table_rows = currency_table.find_all("tr")
    for row in currency_table_rows:
        cols = row.find_all("td")
        cols = [elem.text.strip() for elem in cols]
        try:
            date_ = datetime.strptime(cols[0], "%d.%m.%Y")
            print(type(cols[-1]))
            data_[date_] = float(cols[-1].replace(",", "."))
        except (IndexError, ValueError):
            pass
    print(data_)


if __name__ == "__main__":
    main()
