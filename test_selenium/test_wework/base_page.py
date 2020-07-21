# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    _driver = None
    _base_url = ""

    def __init__(self, driver: webdriver = None):
        if driver is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=option)
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_condition(self, condition):
        WebDriverWait(self._driver, 10).until(condition)
