import os
import yaml


def get_project_path():
    """获取项目路径"""
    realpath = os.path.dirname(__file__).split('common')[0]
    return realpath


def read_config_yaml(one_name, two_name):
    """去读全局配置yaml文件"""
    with open(str(get_project_path()) + 'config.yaml', 'r', encoding='utf-8') as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
        return cfg[one_name][two_name]


def read_extract_yaml(one_name):
    """读取提取变量yaml文件"""
    with open(str(get_project_path()) + 'extract.yaml', 'r', encoding='utf-8') as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
        return cfg[one_name]


def write_extract_yaml(extract_dict):
    """向提取变量yaml文件写入数据"""
    with open(str(get_project_path())+'extract.yaml', 'a') as f:
        yaml.dump(extract_dict,f)


def clear_extract_yaml():
    """清空yaml文件所有数据"""
    with open(str(get_project_path())+'extract.yaml', 'w') as f:
        f.truncate()

# 此文件随着项目的需求还可能封装一些项目当中需要到的公共方法,如:
# MD5加密
# 生成时间字符串
# 生成随机手机号码
