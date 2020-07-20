# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from test_selenium.test_wework.base_page import Base


class AddMember(Base):

    def add_member(self):
        """
        添加成员页面
        :return:
        """
        self.find(By.ID, 'username').send_keys("xz")
        self.find(By.ID, 'memberAdd_acctid').send_keys("xz812964793")
        self.find(By.ID, 'memberAdd_phone').send_keys("15711111111")
        self.find(By.XPATH, '//*[@class="js_member_editor_form"]/div[3]/a[2]').click()
