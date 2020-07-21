# -*- coding: utf-8 -*-
from test_selenium.test_wework.wework_pageObject.index_po import Index


class TestAddMember:

    def setup(self):
        self.index = Index()

    def test_add_member(self):
        """
        测试添加成员
        :return:
        """
        # self.index.goto_add_member().add_member()
        self.index.goto_add_member2().add_member()