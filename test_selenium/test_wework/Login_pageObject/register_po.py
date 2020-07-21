# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from test_selenium.test_wework.base_page import Base


class Register(Base):

    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def register(self):
        """
        注册页面
        :return:
        """
        self.find(By.ID, 'corp_name').send_keys('esensoft')
        self.find(By.ID, 'corp_industry').click()
        self.find(By.XPATH, '//*[@data-name="IT服务"]').click()
        self.find(By.XPATH, '//*[@data-name="计算机软件/硬件/信息服务"]').click()
        self.find(By.ID, 'manager_name').send_keys("xz")
        return True
