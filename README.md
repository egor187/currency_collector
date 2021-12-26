Data-scraper для сбора информации о курсе валют с официального сайта ЦБР.

Стэк:
    - python 3.10
    - postgresql
    - selenium webdriver
    - sqlalchemy
    - BeautifulSoup

Приложения упаковано в docker image

Инструкция по использованию:

1. Clone docker-compose-prod.yml

2. Запуск приложения (cli) ->  "docker-compose -f .\docker_compose_prod.yml run --rm app python run.py <CURRENCYNAME>"
