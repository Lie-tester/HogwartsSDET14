# -*- coding: utf-8 -*-
import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testwork():
    """
    cookie的使用
    """
    def setup(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('霍格沃兹测试学院')
        sleep(2)
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.find_element_by_link_text('霍格沃兹测试学院 – 测试开发工程师的黄埔军校').click()
        sleep(2)

    def test_wework(self):
        # 要打开登陆后的url，并进行刷新；企业微信首页获取cookie后刷新是不会跳转到登陆后的页面的
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'Cf32flUZRaMLgBu-mXos-n7IkWCYoWnSBUY2L-Q086uvHE0GAGR-HyiDybklmzRbI1zeByz5wxXvNEXLoz1qZlLOvrMADWC1JsI7N2FcuvIXY0dKln3-UKDmO4JKNX-KAd6D5qLrre8FMB220XBmz-gIGXDQh593kq9Lc0rSWnasRFJuyJ2IUe1t6JmUujitzJsEjnPE0f_z4Bq3GRqcrhxktvYI-cYY1RJf8DOQ7tqMnT7Nqo53GpElQM_87V-26-kWHjnuhWS2198WwJkKAQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '6meavJV3VBoW_jYIyrMKSZhlYlVlviy4h2b9IVPJcnAbCm1Ko9dVexydb9C24C32'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8748411'}, {'domain': '.qq.com', 'expiry': 1595084641, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850372151987'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850372151987'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325014146074'}, {'domain': '.work.weixin.qq.com', 'expiry': 1626620050, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1595082764,1595084050'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1595084050'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '8785491093243263'}, {'domain': '.qq.com', 'expiry': 1595170995, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.369722591.1595082741'}, {'domain': 'work.weixin.qq.com', 'expiry': 1595114272, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '1idevk'}, {'domain': '.qq.com', 'expiry': 1658156595, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.11530701.1595082741'}, {'domain': '.work.weixin.qq.com', 'expiry': 1595114272, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1597676598, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
        # print(self.driver.get_cookies())
        # 打开数据库
        db = shelve.open("cookies")
        # 将cookies存入数据库，生成文件
        # db["cookies"] = cookies
        # 取出cookies
        cookies = db["cookies"]
        for cookie in cookies:
            # 经测试可以不需要这段代码
            # if "expiry" in cookie.keys():
            #     cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(2)
        self.driver.find_element_by_id('menu_contacts').click()
        sleep(2)
        self.driver.execute_script('window.alert("查看通讯录")')
        sleep(2)
