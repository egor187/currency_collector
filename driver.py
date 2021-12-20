from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Driver:
    def __init__(self):
        self.wb_options = webdriver.ChromeOptions()
        self.wb_options.page_load_strategy = "normal"
        self.wb_options.add_argument("--headless")
        self.wb_options.add_argument("--disable-gpu")

    def get_local_driver(self):
        return webdriver.Chrome(options=self.wb_options)

    def get_remote_driver(self):
        driver = webdriver.Remote(
            command_executor="http://172.26.0.3:4444",
            options=self.wb_options
        )
        return driver
