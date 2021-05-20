import yaml


class ReadExtract:
    def read_extract(self):
        with open('../tools/extract.yaml', encoding='utf-8') as f:
            result = yaml.load(stream=f, Loader=yaml.FullLoader)
            # dict对象
            return result

    def write_extract(self, data):
        with open('../tools/extract.yaml', encoding='utf-8', mode='w') as f:
            yaml.dump(data, stream=f, allow_unicode=True)
