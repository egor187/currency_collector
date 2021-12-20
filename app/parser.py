from datetime import datetime

from bs4 import BeautifulSoup


def parse_currency_html(currency_html: str) -> dict:
    data_ = dict()

    currency_table = BeautifulSoup(currency_html, "html.parser").find("table", class_="data").find("tbody")
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
    return data_
