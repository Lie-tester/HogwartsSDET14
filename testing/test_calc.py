# -*- coding: utf-8 -*-
# 测试用例
import sys
import allure
import pytest
import yaml

print(sys.path.append('..'))
from pythoncode.calc import Calculator

with open("./data/data.yml") as f:
    datas = yaml.safe_load(f)
    addids = datas["add"].keys()
    adddatas = datas["add"].values()
    decids = datas["dec"].keys()
    decdatas = datas["dec"].values()
    divids = datas["div"].keys()
    divdatas = datas["div"].values()
    mulids = datas["mul"].keys()
    muldatas = datas["mul"].values()


# @allure.feature("计算器")
class TestCalc:

    def setup_class(self):
        self.cal = Calculator()

    # def teardown_class(self):
    #     self.cal = Calculator()

    # @pytest.mark.parametrize("a, b", adddatas
    #     , ids=addids)
    # @pytest.mark.add
    # @allure.story("加法运算")
    @pytest.mark.first
    @pytest.mark.dependency(name='add')
    def test_add(self, add):
        if type(add[0]) == str or type(add[1]) == str:
            try:
                self.cal.add(add[0], add[1])
            except Exception:
                assert True
            else:
                assert False
        else:
            result = add[0] + add[1]
            assert self.cal.add(add[0], add[1]) == result

    # @pytest.mark.parametrize("a, b", decdatas
    #     , ids=decids)
    # @pytest.mark.dec
    # @allure.story("减法运算")
    @pytest.mark.second
    @pytest.mark.dependency(depends=["add"])
    def test_dec(self, dec):
        if type(dec[0]) == str or type(dec[1]) == str:
            try:
                self.cal.dec(dec[0], dec[1])
            except Exception:
                assert True
            else:
                assert False
        else:
            result = dec[0] - dec[1]
            assert self.cal.dec(dec[0], dec[1]) == result

    # @pytest.mark.parametrize("a, b", muldatas
    #     , ids=mulids)
    # @pytest.mark.mul
    # @allure.story("乘法运算")
    @pytest.mark.third
    @pytest.mark.dependency(name='mul')
    def test_mul(self, mul):
        if type(mul[0]) == str or type(mul[1]) == str:
            try:
                self.cal.mul(mul[0], mul[1])
            except Exception:
                assert True
            else:
                assert False
        else:
            result = mul[0] * mul[1]
            assert self.cal.mul(mul[0], mul[1]) == result

    # @pytest.mark.parametrize("a, b", divdatas
    #     , ids=divids)
    # @pytest.mark.div
    # @allure.story("除法运算")
    @pytest.mark.fourth
    @pytest.mark.dependency(depends=["mul"])
    def test_div(self, div):
        if type(div[0]) == str or type(div[1]) == str or div[1] == 0:
            try:
                self.cal.div(div[0], div[1])
            except Exception:
                assert True
            else:
                assert False
        else:
            result = div[0] / div[1]
            assert self.cal.div(div[0], div[1]) == result

    @pytest.mark.first
    def check_test(self):
        print("check_*开头的用例也会执行")

    def test_env(self,mycmdoption):
        print("环境验证")
        myenv, datas = mycmdoption
        print(f"环境：{myenv} , 数据：{datas}")
        ip = datas['env']['ip']
        port = datas['env']['port']
        url = 'http://'+str(ip)+':'+str(port)
        print(url)

    if __name__ == '__main__':
        pytest.main()
