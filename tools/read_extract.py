import yaml


class ReadExtract:
    def __init__(self, path, param=None):
        self.path = path
        self.param = param

    def get_data(self):
        with open(self.path, "rb") as y:
            cont = y.read()                         # 获取yaml文件中的所有信息
        yaml.warnings({'YAMLLoadWarning': False})   # 禁用加载器warnings报警
        cf = yaml.load(cont)                        # 将bytes格式转换成dict格式
        y.close()                                   # 关闭文件
        if self.param is None:
            return cf                               # 返回所有数据
        else:
            return cf.get(self.param)               # 获取键为param的值




    def read_extract(self):
        with open('../tools/extract.yaml', encoding='utf-8') as f:
            result = yaml.load(stream=f, Loader=yaml.FullLoader)
            # dict对象
            return result

    def write_extract(self, data):
        with open('../tools/extract.yaml', encoding='utf-8', mode='a') as f:
            yaml.dump(data, stream=f, allow_unicode=True)
