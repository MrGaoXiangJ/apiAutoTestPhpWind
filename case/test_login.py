"""
    目标：完成登录业务层实现
"""

# 导包 unittest ApiLogin
import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson


# 读取数据函数
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

        # 调试使用
        print("查看相应结果:", s.reason)
        print('文件类型:', type(s))

        # 断言 响应信息 及 状态码
        self.assertEquals("OK", s.reason)
        # self.assertEquals(expect_result, s.json()['message'])
        # 断言响应状态码
        # self.assertEquals(201, s.status_code)
        # self.assertEquals(status_code, s.status_code)


if __name__ == '__main__':
    unittest.main()
