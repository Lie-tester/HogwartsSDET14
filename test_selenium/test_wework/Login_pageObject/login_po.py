# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from test_selenium.test_wework.base_page import Base
from test_selenium.test_wework.Login_pageObject.register_po import Register


class Login(Base):

    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def scan(self):
        """
        扫码登陆
        :return:
        """
        pass

    def register(self):
        """
        企业注册
        :return:
        """
        self.find(By.XPATH, '//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        return Register(self._driver)
