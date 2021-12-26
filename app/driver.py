import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv, find_dotenv


class WBDriver:
    def __init__(self, currency_code: str, first_year_search: str) -> None:
        load_dotenv(find_dotenv())
        self.url = os.getenv("CBR_URL")
        self.web_driver_remote_url = os.getenv("WB_DRIVER_REMOTE_URL")
        self.wb_options = webdriver.ChromeOptions()
        self.wb_options.page_load_strategy = "normal"
        self.wb_options.add_argument("--headless")
        self.wb_options.add_argument("--disable-gpu")
        self.currency_code = currency_code
        self.first_year_search = first_year_search

    def get_driver(self) -> webdriver:
        return webdriver.Chrome(options=self.wb_options)

    def get_currency_html(self) -> str:
        driver = self.get_driver()
        driver.delete_all_cookies()
        driver.get(self.url)
        driver.set_page_load_timeout(10)

        currency_selector = driver.find_element(By.ID, "UniDbQuery_VAL_NM_RQ")
        cur_select_obj = Select(currency_selector)
        cur_select_obj.select_by_value(self.currency_code)

        driver.find_element(By.CLASS_NAME, "datepicker-filter_button").click()
        driver.implicitly_wait(5)
        year_selector = driver.find_element(
            By.XPATH, '/html/body/main/div/div/div/form/div/div[1]/div[4]/div/label/div[1]/div/div[3]/div[1]/div/div/div/select[2]'
        )
        driver.implicitly_wait(5)
        year_select_obj = Select(year_selector)
        year_select_obj.select_by_index(0)

        driver.find_element(
            By.XPATH, "/html/body/main/div/div/div/form/div/div[1]/div[4]/div/label/div[1]/div/div[3]/div[1]/div/table/tbody/tr[1]/td[7]/a"
        ).click()
        driver.implicitly_wait(5)
        driver.find_element(By.CLASS_NAME, "datepicker-filter_apply-btn").click()
        driver.implicitly_wait(5)

        driver.find_element(By.ID, "UniDbQuery_searchbutton").click()
        html = driver.page_source
        driver.quit()
        return html


class RemoteWBDriver(WBDriver):
    def __init__(self, currency_code: str, first_year_search: str):
        super().__init__(currency_code, first_year_search)

    def get_driver(self):
        driver = webdriver.Remote(
            command_executor=self.web_driver_remote_url,
            options=self.wb_options
        )
        return driver

