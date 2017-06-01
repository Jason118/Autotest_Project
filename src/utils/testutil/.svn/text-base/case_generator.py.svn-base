# -*- coding: utf-8 -*-
"""此类用来生成测试文件，从数据文件中读取测试用例，从xml中读取接口配置，组织到测试文件中。

一个接口是一个class，每一条测试用例是一个method。

"""

from src.utils.filereader.file_reader import *
from src.utils.config import DefaultConfig, Config
from src.utils.logger import Logger
from src.utils.utils_exception import UnSupportFileType, NoSectionError, NoOptionError
from src.utils.filereader.parsing import *
from src.utils.filereader.generators import parse_generator
from src.utils.testutil.tests import RestTest
from src.utils.testutil.testset import TestConfig, TestSet


DATA_PATH = DefaultConfig().data_path
logger = Logger(__name__).get_logger()


def parse_testsets(base_url, test_structure, vars=None):
    """ 将从YAML里读出来的Python数据结构的数据转化成一个testset列表
    这个数据结构是一个字典的列表，其中描述：
        - test
        - simple test（仅仅是一个URL，是一个最小的test）
        - config（所有test的通用配置）

    返回一个testsets的列表。
    """
    testsets = list()

    for test_set in test_structure:

        test_config = TestConfig()
        # tests = list()
        tests_out = list()

        if vars and isinstance(vars, dict):
            test_config.variable_binds = vars

        for node in test_set:  # 取出每一个节点，进行解析

            if isinstance(node, dict):  # 每一个节点均为一个dict
                node = lowercase_keys(node)

                for key in node:
                    if key == 'config':
                        # 如果是 config 标签，对其进行configuration解析
                        test_config = parse_configuration(node[key], base_config=test_config)
                    elif key == 'url':
                        mytest = RestTest()
                        val = node[key]
                        assert isinstance(val, basestring)
                        mytest.url = base_url + val
                        tests_out.append(mytest)
                    elif key == 'test':
                        child = node[key]
                        mytest = RestTest.parse_test(base_url, child)
                        tests_out.append(mytest)
        testset = TestSet()
        testset.tests = tests_out
        testset.config = test_config
        testsets.append(testset)
    return testsets


def parse_configuration(node, base_config=None):
    """ Parse input config to configuration information """
    test_config = base_config
    if not test_config:
        test_config = TestConfig()

    node = lowercase_keys(flatten_dictionaries(node))  # Make it usable

    for key, value in node.items():
        if key == u'print_bodies':
            test_config.print_bodies = safe_to_bool(value)
        elif key == u'variable_binds':
            if not test_config.variable_binds:
                test_config.variable_binds = dict()
            test_config.variable_binds.update(flatten_dictionaries(value))
        elif key == u'generators':
            flat = flatten_dictionaries(value)
            gen_map = dict()
            for generator_name, generator_config in flat.items():
                gen = parse_generator(generator_config)
                gen_map[str(generator_name)] = gen
            test_config.generators = gen_map
        elif key == u'testset':
            test_config.test = value
        elif key == u'run':
            test_config.run = safe_to_bool(value)
        elif key == u'headers':
            test_config.headers = safe_to_json(flatten_dictionaries(value))

    return test_config


def parse_headers(header_string):
    """ Parse a header-string into individual headers
        Implementation based on: http://stackoverflow.com/a/5955949/95122
        Note that headers are a list of (key, value) since duplicate headers are allowed

        NEW NOTE: keys & values are unicode strings, but can only contain ISO-8859-1 characters
    """
    # First line is request line, strip it out
    if not header_string:
        return list()
    request, headers = header_string.split('\r\n', 1)
    if not headers:
        return list()

    from email import message_from_string
    header_msg = message_from_string(headers)
    # Note: HTTP headers are *case-insensitive* per RFC 2616
    return [(k.lower(), v) for k, v in header_msg.items()]

'''
class Generator(object):
    """测试生成器基本类"""
    def __init__(self, project):
        """

        :param project: 项目名称
        """
        self.proj_name = project

        self.conf_file = 'config_{}.ini'.format(self.proj_name)
        self.cf = Config(self.conf_file)

        self.test_file_name = 'test_{}.py'.format(self.proj_name)

    import_string = "# -*- coding: utf-8 -*-\nimport unittest\nimport json\n"
    class_string = "\nclass Test{}(unittest.TestCase):\n"
    tab = "    "
    setup_string = "\n    def setUp(self):\n"
    teardown_string = "\n    def tearDown(self):\n"
    class_setup_string = "\n    def setUpClass(cls):\n"
    class_teardown_string = "\n    def tearDownClass(cls):\n"
    test_method_string = "\n    def test_{}_{}(self):\n"


class InterfaceTestCaseGenerator(Generator):
    """测试类生成器"""
    logger = Logger(__name__).get_logger()

    def __init__(self, project):
        """初始化生成器，传入项目名称，获取相应配置文件、数据文件、接口文件"""
        Generator.__init__(self, project)

        self.case_file = self.cf.get('file', 'interfaces')
        self.case_file_type = self.case_file.split('.').pop()

        if self.case_file_type in ['yaml', 'yml']:
            self.interface_reader = YamlReader(self.case_file)
        elif self.case_file_type == 'xml':
            self.interface_reader = XMLReader(self.case_file)
        else:
            self.logger.exception(UnSupportFileType(u'不支持的用例文件类型，请检查配置文件！'))

        try:
            self.encrypt = self.cf.get('encrypt', 'encrypt')
        except (NoSectionError or NoOptionError):
            self.encrypt = False
        if self.encrypt:
            self.private_key = self.cf.get('encrypt', 'private_key')
            self.salt = self.cf.get('encrypt', 'salt')

    def generate(self):
        with open(self.test_file, 'wb') as test_file:
            test_file.write(self.import_string)
            for tag in self.tags:
                # interface = self.interface_reader.get_url(tag)

                class_string = self.get_class(tag)
                test_file.write(class_string)

                test_file.write('\n\n\n')

    @property
    def import_string(self):
        import_string = """# -*- coding: utf-8 -*-\nimport unittest\nimport json\n"""
        rest_flag = webservice_flag = socket_flag = 0
        for tag in self.tags:
            interface_type = self.interface_reader.get_type(tag).lower()
            if interface_type in ['rest', 'restful', 'http']:
                rest_flag = 1
            elif interface_type == 'webservice':
                webservice_flag = 1
            elif interface_type in ['tcp', 'socket']:
                socket_flag = 1
            else:
                self.logger.error(u'没有找到合适的接口类型')
        if rest_flag:
            import_string += 'import requests\n'
        if webservice_flag:
            import_string += 'import suds\n'
        if socket_flag:
            import_string += 'import socket\n'
        import_string += 'from src.utils.logger import Logger\n\n'
        return import_string

    def get_class(self, tag):
        data_file = self.interface_reader.get_file(tag)
        sheet = self.interface_reader.get_sheet(tag)
        excel_reader = ExcelReader(data_file, sheet=sheet)

        interface_type = self.interface_reader.get_type(tag).lower()

        class_string = 'class Test%s(unittest.TestCase):\n\n' % tag

        # todo: rest webservice socket

        if interface_type in ['rest', 'restful', 'http']:
            setup_string = self.get_rest_setup(tag)
            cases_string = ''
            teardown_string = self.get_rest_teardown(tag)

            for num, case in enumerate(excel_reader.data):
                case_string = self.get_rest_test(tag, num, case)
                cases_string += case_string

            class_string += setup_string + teardown_string + cases_string
        return class_string

    def get_rest_setup(self, tag):
        setup_string = """    def setUp(self):\n        session = requests.session()\n\n"""
        return setup_string

    def get_rest_teardown(self, tag):
        teardown_string = """    def tearDown(self):\n        pass\n\n"""
        return teardown_string

    def get_rest_test(self, tag, num, case):
        method = self.interface_reader.get_method(tag)
        interface_url = self.interface_reader.get_url(tag)
        test_string = """    def test_%s_%d(self):\n        pass\n\n""" % (tag, num)
        return test_string

    def get_setup(self, interface):
        pass

    def get_test(self, interface):
        pass

    def get_teardown(self, interface):
        pass
'''
