import logging
import time
from common.common_util import get_project_path,read_config_yaml

class LoggerUtil:
    """初始化文件和控制台的日志对象,日志级别,日志文件路径,日志格式等"""
    def __init__(self,loggerName=None):
        # 创建一个logger,loggerName就是给这个logger起一个名字
        self.logger = logging.getLogger(loggerName)
        # 设置全局日志级别为DEBUG
        self.logger.setLevel(logging.DEBUG)
        # 设置日志文件的输入路径和名称
        self.log_path = get_project_path()+'log/'
        self.log_time = time.strftime("%Y-%m-%d")
        self.log_path_and_name = self.log_path+read_config_yaml('log','log_name'+self)
        # 创建文件和控制台日志处理器
        self.file_hander = None
        self.console_hander = None

    def creat_file_log(self):
        pass