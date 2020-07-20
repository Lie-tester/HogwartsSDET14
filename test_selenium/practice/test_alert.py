# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains

from test_selenium.practice.test_base import Base


class Testalert(Base):

    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')

        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(2)
