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
    @pytest.mark.parametrize("a,b,result", yaml.safe_load(open("./data/add.yaml"))
        , ids=[f"第{i}组" for i in range(1,6)])
    @pytest.mark.add
    @allure.story("加法运算")
    def test_add(self, a, b, result):
        # cal = Calculator()
        assert self.cal.add(a, b) == result

    @pytest.mark.parametrize("a,b,result", yaml.safe_load(open("./data/dec.yaml"))
        , ids=[f"第{i}组" for i in range(1,6)])
    @pytest.mark.dec
    @allure.story("减法运算")
    def test_dec(self, a, b, result):
        # cal = Calculator()
        assert self.cal.dec(a, b) == result

    @pytest.mark.parametrize("a,b,result", yaml.safe_load(open("./data/mul.yaml"))
        , ids=[f"第{i}组" for i in range(1,6)])
    @pytest.mark.mul
    @allure.story("乘法运算")
    def test_mul(self, a, b, result):
        # cal = Calculator()
        # print(self.cal.mul(a, b))
        assert self.cal.mul(a, b) == result

    @pytest.mark.parametrize("a,b,result", yaml.safe_load(open("./data/div.yaml"))
        , ids=[f"第{i}组" for i in range(1,6)])
    @pytest.mark.div
    @allure.story("除法运算")
    def test_div(self, a, b, result):
        # cal = Calculator()
        assert self.cal.div(a, b) == result


if __name__ == '__main__':
    pytest.main()
