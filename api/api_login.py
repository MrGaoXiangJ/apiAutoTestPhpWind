"""
    目标：实现登录接口对象封装
"""

# 导包 requests
import requests


# 新建类 登录接口对象
class ApiLogin(object):
    # 新建方法 登录方法
    def api_post_login(self, url, step, pwuser, pwpwd, lgt):
        requestData = (f"jumpurl=http://localhost/phpwind/index.php&step={step}&pwuser={pwuser}&pwpwd={pwpwd}&head_login=''&lgt={lgt}")
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        # 调用post并返回响应对象
        return requests.post(url, headers=headers, data=requestData)


"""
    提示：
        url、mobile、code:最后都需要从data数据文件读取出来，做参数化使用，所以这里我们动态传参
"""