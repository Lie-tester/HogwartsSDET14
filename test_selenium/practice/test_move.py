# -*- coding: utf-8 -*-
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from test_selenium.practice.test_base import Base


class TestMove(Base):

    def test_moveto(self):
        self.driver.get('https://www.baidu.com')
        ele = self.driver.find_element_by_id('s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(ele).perform()
        sleep(2)

    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag = self.driver.find_element_by_id('dragger')
        to_drag = self.driver.find_element_by_xpath('/html/body/div[3]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, to_drag).perform()
        sleep(3)

    def test_copy(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        user1 = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        user2 = self.driver.find_element_by_xpath('/html/body/label[2]/table/tbody/tr/td[2]/input')
        user1.click()
        action = ActionChains(self.driver)
        action.send_keys('username')
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('xz').pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)
        action.move_to_element(user2).click().pause(1)
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).pause(1)
        action.send_keys(Keys.SPACE)
        action.send_keys('copy').perform()
        sleep(2)
