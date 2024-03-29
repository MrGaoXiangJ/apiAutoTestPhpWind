# 导包 json
import json

# 打开josn文件并获取文件流
# with open("../data/login.json", "r", encoding="utf-8") as f:
#     # 调用load方法加载文件流
#     data = json.load(f)
#     print("获取的数据为：", data)

# 使用函数进行封装
# def read_json():
#     with open("../data/login.json", "r", encoding="utf-8") as f:
#         # 调用load方法加载文件流
#         return json.load(f)


# 使用参数替换 静态文件名

class ReadJson(object):

    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8-sig") as f:
            # 调用load方法加载文件流
            return json.load(f)



"""
    问题：
        1. 未经过封装无法在别的模块内使用。
        2. 数据存储文件有好几个，如果写次，在读取别的文件时无法使用
        3. 预期格式为列表嵌套元祖 [(url,mobile,code...)],目前返回字典？
    解决：
        1. 进行封装
        2. 使用参数替换静态写死的文件名
        3. 读取字典内容，并添加到新的列表中。
"""

if __name__ == '__main__':
    print(ReadJson("login_more.json").read_json())
