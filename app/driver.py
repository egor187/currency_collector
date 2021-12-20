import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv, find_dotenv


class WBDriver:
    def __init__(self, currency_code: str) -> None:
        load_dotenv(find_dotenv())
        self.url = os.getenv("CBR_URL")
        self.web_driver_remote_url = os.getenv("WB_DRIVER_REMOTE_URL")
        self.wb_options = webdriver.ChromeOptions()
        self.wb_options.page_load_strategy = "normal"
        self.wb_options.add_argument("--headless")
        self.wb_options.add_argument("--disable-gpu")
        self.currency_code = currency_code

    def get_driver(self) -> webdriver:
        return webdriver.Chrome(options=self.wb_options)

    def get_currency_html(self) -> str:
        driver = self.get_driver()
        driver.get(self.url)
        currency_selector = driver.find_element(By.ID, "UniDbQuery_VAL_NM_RQ")
        select_obj = Select(currency_selector)
        select_obj.select_by_value(self.currency_code)
        driver.find_element(By.ID, "UniDbQuery_searchbutton").click()
        html = driver.page_source
        return html


class RemoteWBDriver(WBDriver):
    def __init__(self, currency_code: str):
        super().__init__(currency_code)

    def get_driver(self):
        driver = webdriver.Remote(
            command_executor=self.web_driver_remote_url,
            options=self.wb_options
        )
        return driver

