# -*- coding: utf-8 -*-
"""解析配置文件，获取配置

实例化Config类，并传入相应config文件路径。可获取config文件中的配置项。

For example:

    cf = Config(path='D:\py\AutoTestFramework\config\config.ini')
    print cf.get('path', '')


实例化DefaultConfig类，可获取指定一些配置做为属性，可直接访问该属性，能够简便许多。

For example:

    cf = DefaultConfig()
    print cf.db_connect
    print cf.log_path

"""

import os
from ConfigParser import ConfigParser, NoSectionError, NoOptionError
from src.utils.utils_exception import ConfigFileException, ConfigError
import pymysql


# 获取当前文件绝对路径，从而获得config层路径
UTILS_PATH = os.path.split(os.path.realpath(__file__))[0]

# print 'utils_path-->',UTILS_PATH
BASE_PATH = UTILS_PATH +'/../..'
CONFIG_PATH = UTILS_PATH + '/../../config/'  # config层
# print CONFIG_PATH


# print os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/config'
# CONFIG_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/config/'


class Config(ConfigParser):
    def __init__(self, filename='config.ini'):
        ConfigParser.__init__(self)
        self.path = CONFIG_PATH + filename
        if os.path.exists(self.path):
            self.read(self.path)
        else:
            raise ConfigFileException('Config file not exists or not available.Please check {}.'.format(self.path))

#     def _mysql_connect(self):
#         """Get sqlalchemy database connection string."""  #'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
# #         return 'mysql+{0}://{1}:{2}@{3}:{4}/{5}?charset=utf8'.format(
# #         config = configparser.ConfigParser()
# 
#         # 从配置文件中读取数据库服务器IP、域名，端口
# #         config.read(config_file)
#         self.driver = self.get('db', 'driver')
#         self.host = self.get('db', 'host')
#         self.port = self.get('db', 'port')
#         self.user = self.get('db', 'user')
#         self.passwd = self.get('db', 'pwd')
#         self.db = self.get('db', 'db_name')
#         self.charset = self.get('db', 'charset')
# #         print 'okkkk',self.host,self.port,self.user,self.passwd,self.db,self.charset
# #         print(host=self.host, port=int(self.port), user=self.user, password=self.passwd, database=self.db, charset=self.charset)
#         conn = pymysql.connect(host=self.host, port=int(self.port), user=self.user, password=self.passwd, database=self.db, charset=self.charset)
#         return conn
# #         return '{0}+pymysql://{1}:{2}@{3}:{4}/{5}?charset={6}'.format(
# #             self.get('db', 'driver'),
# #             self.get('db', 'user'),
# #             self.get('db', 'pwd'),
# #             self.get('db', 'host'),
# #             self.get('db', 'port'),
# #             self.get('db', 'db_name'),
# #             self.get('db', 'charset')
# #         )
# 
#     def _oracle_connect(self):
#         """Get Oracle database connection string."""
#         return '{0}/{1}@{2}:{3}/{4}'.format(
#             self.get('db', 'user'),
#             self.get('db', 'pwd'),
#             self.get('db', 'host'),
#             self.get('db', 'port'),
#             self.get('db', 'db_name')
#         )
# 
#     @property
#     def db_connect(self):
#         db_driver = self.get('db', 'driver').lower()
#         try:
#             if db_driver == 'mysql':
# #                 print '_mysql_connect--->',self._mysql_connect()
#                 return self._mysql_connect()
#             elif db_driver == 'oracle':
#                 return self._oracle_connect()
#         except NoSectionError and NoOptionError:
#             raise ConfigError('[db] section is required. And [db] section must have these options:'
#                               '"driver", "user", "pwd", "host", "port", "db_name"')


class DefaultConfig(Config):
    """
        -properties:
            db_connect  : Return database string which can use to connect to database.
            base_path   : Return [path].base value.
            log_path    : Return [path].log value or default log path.
            report_path : Return [path].report value or default report path.
            data_path   : Return [path].data value or default data path.
            driver_path : Return default driver path.
    """
    def __init__(self):
        Config.__init__(self)

    @property
    def base_path(self):
        return BASE_PATH
#         try:
#             return BASE_PATH
#         except NoSectionError and NoOptionError:
#             raise ConfigError('[path] section and "base" option is required.')

    @property
    def log_path(self):
        return self.base_path + '/log/'
#         try:
#             return self.get('path', 'log')
#         except NoSectionError and NoOptionError:
#             return self.base_path + '/log/'

    @property
    def report_path(self):
        return self.base_path + '/report/'
#         try:
#             return self.get('path', 'report')
#         except NoSectionError and NoOptionError:
#             return self.base_path + '/report/'

    @property
    def data_path(self):
        return self.base_path + '/data/'
#         try:
#             return self.get('path', 'data')
#         except NoSectionError and NoOptionError:
#             return self.base_path + '/data/'

    @property
    def driver_path(self):
        return self.base_path + '/drivers/'
    
    @property
    def test_environment(self):
        return self.get('testEnvironment', 'environment')


class Config_Project(ConfigParser):
    
    project_filename = 'project_' + DefaultConfig().test_environment +'.ini'    #project_filename = 'project_ysc.ini'
    def __init__(self, filename=project_filename):
        ConfigParser.__init__(self)
        self.path = CONFIG_PATH + filename
        if os.path.exists(self.path):
            self.read(self.path)
        else:
            raise ConfigFileException('Config_Zhigou file not exists or not available.Please check {}.'.format(self.path))

#     def _mysql_connect(self):
#         """Get sqlalchemy database connection string."""
#         return 'mysql+{0}://{1}:{2}@{3}:{4}/{5}?charset=utf8'.format(
#             self.get('db', 'driver'),
#             self.get('db', 'user'),
#             self.get('db', 'pwd'),
#             self.get('db', 'host'),
#             self.get('db', 'port'),
#             self.get('db', 'db_name')
#         )
# 
#     def _sqlserver_connect(self):
#         """Get sqlserver database connection string."""   #'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
#         return 'mssql+pymssql://{0}:{1}@{2}:{3}/{4}?charset={5}'.format(
#             self.get('db', 'user'),
#             self.get('db', 'pwd'),
#             self.get('db', 'host'),
#             self.get('db', 'port'),
#             self.get('db', 'db_name'),
#             self.get('db', 'charset')
#         )
# 
#     @property
#     def db_connect(self):
#         db_driver = self.get('db', 'driver').lower()
#         try:
#             if db_driver == 'mysql':
#                 print '_mysql_connect--->',self._mysql_connect()
#                 return self._mysql_connect()
#             elif db_driver == 'sqlserver':
#                 print '_sqlserver_connect--->',self._sqlserver_connect()
#                 return self._sqlserver_connect()
#         except NoSectionError and NoOptionError:
#             raise ConfigError('[db] section is required. And [db] section must have these options:'
#                               '"driver", "user", "pwd", "host", "port", "db_name"')


class DefaultConfig_Project(Config_Project):
    """
        -properties:
            db_connect  : Return database string which can use to connect to database.
            base_path   : Return [path].base value.
            log_path    : Return [path].log value or default log path.
            report_path : Return [path].report value or default report path.
            data_path   : Return [path].data value or default data path.
            driver_path : Return default driver path.
    """
    def __init__(self):
        Config_Project.__init__(self)

    @property
    def base_url(self):
        try:
            return self.get('url', 'base_url')
        except NoSectionError and NoOptionError:
            raise ConfigError('[path] section and "base" option is required.')
    
#     @property
#     def test_environment(self):
#         return self.get('testEnvironment', 'environment')

    # user info
    @property
    def user_name(self):
        return self.get('users', 'user_name')
    
    @property
    def pass_word(self):
        return self.get('users', 'pass_word')
    
    @property
    def auth_num(self):
        return self.get('users', 'auth_num')

    @property
    def http_host(self):
        return self.get('http', 'host')

    @property
    def http_port(self):
        return self.get('http', 'port')

    

if __name__ == '__main__':
    cf = Config_Project()
    print cf.get('db', 'port')
    print DefaultConfig().base_path
    print DefaultConfig().path
    print Config_Project().path

    defaultcf = DefaultConfig_Project()
#     print defaultcf.db_connect

    print defaultcf.base_url
    print defaultcf.user_name
    print defaultcf.pass_word
    print defaultcf.auth_num
#     print defaultcf.report_path
