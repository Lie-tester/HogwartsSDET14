# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from test_selenium.test_wework.base_page import Base
from test_selenium.test_wework.wework_pageObject.add_member_po import AddMember


class Index(Base):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        """
        添加成员跳转
        :return:
        """
        self.find(By.XPATH, '//*[@class="index_service"]/div[2]/a[1]/div[1]').click()
        return AddMember(self._driver)

    def goto_add_member2(self):
        """
        从首页旁的通讯录跳转
        :return:
        """
        def add_condition(x):
            """
            传入等待条件
            :param x:
            :return:
            """
            # find只会找到元素后返回value,没有返回就没有返回值,直到超时；这里就不会执行if语句
            # 而finds找到元素返回value, 没有找到则返回[]；这里没有找到就会执行if语句
            ele = self.finds(By.ID, 'username')
            # ele_len = len(self.finds(By.ID, 'username'))
            if not ele:
                self.find(By.XPATH, '//*[@class="ww_operationBar"]/a[1]').click()
            else:
                return ele

        self.find(By.ID, 'menu_contacts').click()
        self.wait_condition(add_condition)
        return AddMember(self._driver)

    def goto_imp_address(self):
        """
        导入通讯录跳转
        :return:
        """
        pass

    def goto_join_member(self):
        """
        成员加入跳转
        :return:
        """
        pass
