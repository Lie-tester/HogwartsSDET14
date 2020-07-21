# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from test_selenium.test_wework.base_page import Base
from test_selenium.test_wework.Login_pageObject.login_po import Login
from test_selenium.test_wework.Login_pageObject.register_po import Register


class Index(Base):
    _base_url = "https://work.weixin.qq.com/"

    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def goto_login(self):
        """
        企业登陆跳转
        :return:
        """
        self.find(By.XPATH, '//*[@id="indexTop"]//a').click()
        return Login(self._driver)

    def goto_register(self):
        """
        立即注册跳转
        :return:
        """
        self.find(By.XPATH, '//*[@id="tmp"]/div/a').click()
        return Register(self._driver)
