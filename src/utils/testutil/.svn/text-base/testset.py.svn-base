# -*- coding: utf-8 -*-
import json
from src.utils.filereader.parsing import safe_to_json


class TestConfig(object):
    """ 测试用例配置（从config_xx.ini文件以及yaml配置文件的config段读取） """
    print_bodies = False  # 是否打印响应的body
    print_headers = False  # 是否打印响应的header
    verbose = False
    headers = None  # 通用headers
    test = None

    run = True  # 控制用例是否执行

    # 变量与生成器
    variable_binds = None
    generators = None  # Map of generator name to generator function

    # 加密
    private_key = None
    salt = None
    encrypt = None

    # 数据库连接信息
    db = None
    db_connector = None

    # 这个TestSet的基本url
    base_url = None

    def __str__(self):
        return json.dumps(self, default=safe_to_json)


class TestSet(object):
    """ 一组TestCase，以及这组case的配置 """
    tests = list()
    config = TestConfig()

    def __init__(self):
        self.config = TestConfig()
        self.tests = list()

    def __str__(self):
        return json.dumps(self, default=safe_to_json)
