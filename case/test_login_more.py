import re
import unittest
from time import sleep

import requests
from parameterized import parameterized

from api.api_login import ApiLogin
from tools.read_extract import ReadExtract
from tools.read_json import ReadJson


def get_data():
    datas = ReadJson("login_more.json").read_json()
    # 新建空列表,添加读取json数据
    arrs = []
    # 遍历获取所有value
    for data in datas.values():
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

        # 调试使用=
        verifyDict = {"php_winduser": requests.utils.dict_from_cookiejar(s.cookies)["c7b10_winduser"]}
        ReadExtract().write_extract(verifyDict)
        print(verifyDict)
        sleep(3)

        # print(ReadExtract().read_extract()["verifyhash"])
        # 断言 响应信息 及 状态码assertEquals
        self.assertEquals("OK", s.reason)
        # self.assertEquals(expect_result, s.json()['message'])
        # 断言响应状态码
        self.assertEquals(200, s.status_code)
        # self.assertEquals(status_code, s.status_code)


if __name__ == '__main__':
    unittest.main()
