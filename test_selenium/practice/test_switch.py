# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from test_selenium.practice.test_base import Base


class TestSwitch(Base):

    def test_switchwindows(self):
        # 打开注册页面
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="u1"]/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        # 统计窗口句柄
        windows = self.driver.window_handles
        # 切换到注册页面窗口
        sleep(2)
        self.driver.switch_to_window(windows[1])
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys('xiongBOOS')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__phone').send_keys('15700000000')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__password').send_keys('123456')
        sleep(2)
        # 切换回百度首页
        self.driver.switch_to.window(windows[0])
        sleep(2)
        # 点击登陆
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys('xiongBOOS')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys('123456')
        sleep(2)
        self.driver.find_element_by_id('TANGRAM__PSP_11__memberPass').click()
        sleep(1)
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__submit').click()

