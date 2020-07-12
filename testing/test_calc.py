# -*- coding: utf-8 -*-
# 测试用例
import sys
import allure
import pytest
import yaml

print(sys.path.append('..'))
from pythoncode.calc import Calculator


@allure.feature("计算器")
class TestCalc:

    def setup_class(self):
        self.cal = Calculator()

    # def teardown_class(self):
    #     self.cal = Calculator()

    @pytest.mark.parametrize("a, b", yaml.safe_load(open("./data/add.yaml"))
        , ids=["int", "minus", "float", "bigint", "str", "str and int"])
    @pytest.mark.add
    @allure.story("加法运算")
    def test_add(self, a, b):
        if type(a) == str or type(b) == str:
            try:
                self.cal.add(a, b)
            except Exception:
                assert True
            else:
                assert False
        else:
            result = a + b
            assert self.cal.add(a, b) == result

    @pytest.mark.parametrize("a, b", yaml.safe_load(open("./data/dec.yaml"))
        , ids=["int", "minus", "float", "bigint", "str", "str and int"])
    @pytest.mark.dec
    @allure.story("减法运算")
    def test_dec(self, a, b):
        if type(a) == str or type(b) == str:
            try:
                self.cal.dec(a, b)
            except Exception:
                assert True
            else:
                assert False
        else:
            result = a - b
            assert self.cal.dec(a, b) == result

    @pytest.mark.parametrize("a, b", yaml.safe_load(open("./data/mul.yaml"))
        , ids=["int", "minus", "float", "bigint", "str", "str and int"])
    @pytest.mark.mul
    @allure.story("乘法运算")
    def test_mul(self, a, b):
        if type(a) == str or type(b) == str:
            try:
                self.cal.mul(a, b)
            except Exception:
                assert True
            else:
                assert False
        else:
            result = a * b
            assert self.cal.mul(a, b) == result

    @pytest.mark.parametrize("a, b", yaml.safe_load(open("./data/div.yaml"))
        , ids=["int", "minus", "float", "bigint", "str", "str and int","zero"])
    @pytest.mark.div
    @allure.story("除法运算")
    def test_div(self, a, b):
        if type(a) == str or type(b) == str or b == 0:
            try:
                self.cal.div(a, b)
            except Exception:
                assert True
            else:
                assert False
        else:
            result = a / b
            assert self.cal.div(a, b) == result


if __name__ == '__main__':
    pytest.main()
