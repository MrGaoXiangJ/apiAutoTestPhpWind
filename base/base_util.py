import unittest

from common.common_util import clear_extract_yaml
from common.logger_util import LoggerUtil
from common.request_util import RequestUtil

class BaseUtil(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 生成日志类对象
        cls.lu = LoggerUtil()
        # 获取日志对象
        cls.logger = cls.lu.get_logger()
        # 获得接口请求对象
        cls.httpRequest = RequestUtil(cls.logger)
        # 清空extract.yaml文件中提取的值
        clear_extract_yaml()

    def setUp(self) -> None:
        self.logger.info("-------------------接口测试用例执行开始")

    def tearDown(self) -> None:
        self.logger.info("-------------------接口测试用例执行结束")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.lu.remove_hander() # 移除日志处理器

