"""
    目标：完成登录业务层实现
"""

# 导包 unittest ApiLogin
# import json
import unittest
from time import sleep

import requests.utils

from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_extract import ReadExtract
import re
from tools.read_json import ReadJson


def get_data():
    data = ReadJson("login.json").read_json()
    # 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("jumpurl"),
                 data.get("step"),
                 data.get("pwuser"),
                 data.get("pwpwd"),
                 data.get("lgt")))
    return arrs

# 新建测试类
class TestLogin(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand(get_data())
    def test_login(self, jumpurl, step, pwuser, pwpwd, lgt):

        # 调用登录方法
        s = ApiLogin().api_post_login(jumpurl, step, pwuser, pwpwd, lgt)

        # winduser=AG9dAQ4GAFBTVVZTAwIOCVFRCAVRUg5XBQRbXQVRVwMACGw;
        # print(requests.utils.dict_from_cookiejar(s.cookies))
        winduserKey = "php_winduser_"+pwuser
        # # yaml方式处理接口依赖
        verifyDict = {winduserKey: requests.utils.dict_from_cookiejar(s.cookies)["c7b10_winduser"]}
        ReadExtract().write_extract(verifyDict)
        print(verifyDict)
        # sleep(3)

        # print(ReadExtract().read_extract()["verifyhash"])
        # 断言 响应信息 及 状态码assertEquals
        self.assertEqual("OK", s.reason)
        # self.assertEquals(expect_result, s.json()['message'])
        # 断言响应状态码
        self.assertEqual(200, s.status_code)
        # self.assertEquals(status_code, s.status_code)


if __name__ == '__main__':
    unittest.main()
