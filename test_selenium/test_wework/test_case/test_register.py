# -*- coding: utf-8 -*-
from test_selenium.test_wework.Login_pageObject.index_po import Index


class TestRegister():

    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_register().register()
