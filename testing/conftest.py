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

#自定义动态生成测试用例fixture
def pytest_generate_tests(metafunc: "Metafunc"):
    if "add" in metafunc.fixturenames:
        metafunc.parametrize("add", metafunc.module.adddatas
                             , ids=metafunc.module.addids
                             , scope="function")
    if "dec" in metafunc.fixturenames:
        metafunc.parametrize("dec", metafunc.module.decdatas
                             , ids=metafunc.module.decids
                             , scope="function")
    if "div" in metafunc.fixturenames:
        metafunc.parametrize("div", metafunc.module.divdatas
                             , ids=metafunc.module.divids
                             , scope="function")
    if "mul" in metafunc.fixturenames:
        metafunc.parametrize("mul", metafunc.module.muldatas
                             , ids=metafunc.module.mulids
                             , scope="function")

def pytest_addoption(parser):
    mygroup = parser.getgroup("Lie-tester")     #group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",    #注册一个命令行选项
                      default='st',
                      dest='env',
                      help='set your run env'
                      )

@pytest.fixture(scope='session')
def mycmdoption(request):
    myenv = request.config.getoption("--env", default='st')
    if myenv == "test":
        datapath = 'env/test/data.yml'
    if myenv == "dev":
        datapath = 'env/dev/data.yml'
    if myenv == "st":
        datapath = 'env/st/data.yml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas
