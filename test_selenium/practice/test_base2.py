# -*- coding: utf-8 -*-
import os

from selenium import webdriver


class Base:

    def setup(self):
        browser = os.getenv('browser')
        print(browser)
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
