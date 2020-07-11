# -*- coding: utf-8 -*-
import pytest
import yaml


@pytest.fixture(autouse=True)
def calc_remind():
    print("计算开始")
    yield
    print("\n计算结束\n")

@pytest.fixture()
def login(request):
    user = request.param
    print(f"登陆用户为{user}")
    return user
