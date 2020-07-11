# -*- coding: utf-8 -*-
import allure
import pytest
import yaml

@allure.feature("测试fixture参数化")
@pytest.mark.parametrize('login', yaml.safe_load(open('./data/users.yaml')), indirect=True)
def test_case(login):
    print(f"\n用户{login}已登陆")
