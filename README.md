Data-scraper для сбора информации о курсе валют с официального сайта ЦБР.

Стэк:
    - python 3.10
    - postgresql
    - selenium webdriver
    - sqlalchemy
    - BeautifulSoup

Приложения упаковано в docker image

Инструкция по использованию:

1.Clone repo

2.Запуск приложения ->  a) ./docker-compose build
                         b) ./docker-compose run --rm app python run.py <CURRENCYNAME>

