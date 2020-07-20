# -*- coding: utf-8 -*-
from time import sleep
from selenium.webdriver import ActionChains
from test_selenium.practice.test_base import Base


class TestClick(Base):

    def test_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        ele_click = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        ele_doubleclick = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        ele_rightclick = self.driver.find_element_by_xpath('/html/body/form/input[4]')

        actions = ActionChains(self.driver)
        actions.click(ele_click)
        sleep(2)
        actions.double_click(ele_doubleclick)
        sleep(2)
        actions.context_click(ele_rightclick)
        sleep(2)
        actions.perform()
