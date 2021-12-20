import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv, find_dotenv


class Driver:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.url = os.getenv("CBR_URL")
        self.wb_options = webdriver.ChromeOptions()
        self.wb_options.page_load_strategy = "normal"
        self.wb_options.add_argument("--headless")
        self.wb_options.add_argument("--disable-gpu")

    def get_local_driver(self):
        return webdriver.Chrome(options=self.wb_options)

    def get_remote_driver(self):
        driver = webdriver.Remote(
            command_executor=self.url,
            options=self.wb_options
        )
        return driver
