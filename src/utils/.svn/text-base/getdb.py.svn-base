#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Jason'

import configparser
import pymysql
import pymssql
import sys
import _cpkeywords
import ast
from config import Config_Project,DefaultConfig

class GetDB(object):
    '''配置数据库IP，端口等信息，获取数据库连接'''
    def __init__(self, config_file, db):
        config = configparser.ConfigParser()

        # 从配置文件中读取数据库服务器IP、域名，端口
        config.read(config_file)
        self.driver = config[db]['driver']
        self.host = config[db]['host']
        self.port = config[db]['port']
        self.user = config[db]['user']
        self.passwd = config[db]['passwd']
        self.db = config[db]['db_name']
        self.charset = config[db]['charset']

    def get_conn(self):
        if self.driver == 'mysql':
#             print 'ok mysql'
            try:
#                 conn = pymysql.connect(host='10.10.15.135', port=3306, user='interface_test', password='interface_test', database='interface', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
                conn = pymysql.connect(host=self.host, port=int(self.port), user=self.user, password=self.passwd, database=self.db, charset=self.charset)
                return conn
            except Exception as e:
                print('%s', e)
                sys.exit()
        elif self.driver == 'sqlserver':
#             print 'ok sqlserver'
            try:
#                 conn = pyodbc.connect("DRIVER={SQL Server};CHARSET=UTF8;SERVER=119.9.124.151,3344;PORT=1433;DATABASE=CAT01;UID=Lottery01;PWD=adjIUEd8&D817dpA")                
#                 conn = pyodbc.connect(
#                     r'DRIVER={SQL Server};'
#                     r'CHARSET='+self.charset+';'
#                     r'SERVER='+self.host+';'
#                     r'PORT='+self.port+';'
#                     r'DATABASE='+self.db+';'
#                     r'UID='+self.user+';'
#                     r'PWD='+self.passwd
#                     )
                
                #                 conn = pyodbc.connect("DRIVER={SQL Server};CHARSET=UTF8;SERVER=119.9.124.151,3344;PORT=1433;DATABASE=CAT01;UID=Lottery01;PWD=adjIUEd8&D817dpA")                
#                 conn = pymssql.connect(server, user, password, database)
#                 conn = pymssql.connect(server='119.9.124.151', port=3344, user='Lottery01', password='adjIUEd8&D817dpA', database='CAT01', charset='utf8', as_dict=True)
                conn = pymssql.connect(server=self.host, port=self.port, user=self.user, password=self.passwd, database=self.db, charset= self.charset)
                return conn
            except Exception as e:
                print('%s', e)
                sys.exit()


# aa = r'C:\work\svn\Doc\01CP\11AutoTest\web_autotest_project\src\config\config.ini'
# bb = r'C:\work\svn\Doc\01CP\11AutoTest\web_autotest_project\src\config\project_ysc.ini'
# 返回测试数据库连接
def db_mysql_connect(config_file=None, db='db'):
    if config_file == None:
        config_file = DefaultConfig().path
    return GetDB(config_file, db).get_conn()

# 返回应用数据库连接
def db_sqlserver_connect(config_file=None, db='db'):
    if config_file == None:
        config_file = Config_Project().path    
    return GetDB(config_file, db).get_conn()
    
def db_sql_dict(cursor,sql_one):
    return _cpkeywords.sql_query_dict_one(cursor, sql_one)

def db_sql_update(cursor, sql_one):
    """
    对数据库执行单条语句的UPDATE或者DELETE操作。
    :param cursor: 已有的数据库连接。
    :param sql_one: 字符串形式的sql语句。
    :return: 无返回值。
    """
    _cpkeywords.sql_update_one(cursor, sql_one)

def unicode_dict(data):
    return ast.literal_eval(data)   #unicode dict to dict

def clear(db_conn):
    # 关闭数据库连接
#         print 'ok222'
    db_conn.close()


#db_mysql_conn = db_mysql_connect()


if __name__ == '__main__':
    db1 = db_mysql_connect()
    db1_cursor = db1.cursor()
    sql1 = "select * from interface_case  where caseID='User_CanLogin_1';"
    cc = db_sql_dict(db1_cursor,sql1)
    print cc
