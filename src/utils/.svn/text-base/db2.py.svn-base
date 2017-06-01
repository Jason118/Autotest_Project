# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

import config
import _cpkeywords
import ast




# def db_mysql_connect():
#     # 读取配置，链接数据库，返回session
#     db_con = config.DefaultConfig().db_connect
#     db_session = sessionmaker(bind=create_engine(db_con))
#     return db_session()
def db_mysql_connect():
    # 读取配置，链接数据库，返回session
    conn = config.DefaultConfig().db_connect
#     db_session = sessionmaker(bind=create_engine(db_con))
    cursor = conn.cursor()
    return cursor

# todo
# 数据库基本库


def db_sqlserver_connect():
    db_con = config.DefaultConfig_Project().db_connect
    db_session = sessionmaker(bind=create_engine(db_con))
    return db_session()

def db_sql_dict(cursor,sql_one):
    return _cpkeywords.sql_query_dict_one(cursor, sql_one)

def unicode_dict(data):
    return ast.literal_eval(data)   #unicode dict to dict

if __name__ == '__main__':
    sql_conn = db_mysql_connect()
    print 'sql_conn--->',sql_conn
#     session = sql_conn
    ret=sql_conn.execute('desc interface_case')
#     print ret
    # print ret.fetchall()
    print ret.first()
    sql_conn1 = db_sqlserver_connect()
    print 'sql_conn1--->',sql_conn1
# engine = create_engine('mysql://root:ctyyx@localhost:3306/test')
#     session = sql_conn1()
    ret1=sql_conn1.execute('select top 3 * from  TThirdPayBank')
#     print ret1
    # print ret.fetchall()
    print ret1.first()