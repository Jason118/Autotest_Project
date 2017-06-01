#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' from xlsx to db'''
__author__ = 'Jason'

# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

import xlrd,os,json,testcasedata_xls_old_new,time
import ast 


from src.utils.config import DefaultConfig
from src.utils.getdb import db_mysql_connect,clear


db_mysql_conn = db_mysql_connect()
db_mysql_cursor = db_mysql_conn.cursor()
# print 'sql_conn--->',db1_cursor
# #     session = sql_conn
# db1_cursor.execute("select * from web_autotest_case where caseID like 'CP_WEB_MASTERPG_LOGIN%' and normal = 'Y' and caseID !='CP_WEB_MASTERPG_LOGIN_14' limit 1 ;")
# #     print ret
# # print ret.fetchall()
# print db1_cursor.fetchone()


# aa = DefaultConfig().._mysql_connect(self)
# global_config = Global()
# db1_conn = global_config.get_db1_conn()
# db1_cursor = db1_conn.cursor()
db_mysql_cursor.execute("delete from web_autotest_case")  #删除用例表数据
db_mysql_cursor.execute('commit')

# db.create_engine(user='interface_test', password='interface_test', database='interface')  #连接mysql 数据库 
# db.update("delete from interface_case;")



def create_dict_db(file_name):
    returnData={}
    data=xlrd.open_workbook(file_name)
    for j in range(len(data.sheets())):
        table=data.sheets()[j]
        #读取excel第一行数据作为存入mongodb的字段名
        rowstag=table.row_values(0)
        nrows=table.nrows

        for i in range(1,nrows):
            if table.row_values(i)[13]=='Y' or table.row_values(i)[13]=='是':  #自动化支持
#                 print table.row_values(i)[13]
                #将字段名和excel数据存储为字典形式，并转换为json格式
                returnData[i]=json.dumps(dict(zip(rowstag,table.row_values(i))))
                #通过编解码还原数据
                returnData[i]=json.loads(returnData[i])
                
                cols, args = zip(*returnData[i].iteritems())
#                 sql = 'insert into `%s` (%s) values (%s)' % ('web_autotest_case', ','.join(['`%s`' % col for col in cols]), ','.join(['?' for i in range(len(cols))]))
#                 sql = sql.replace('?', '%s')
#                 print 'args:',args
#                 print 'sql:',sql
#                 print (sql + ' % ' + str(args))
                sql2  = 'insert into `%s` (%s) values (%s)' % ('web_autotest_case', ','.join(['%s' % col for col in cols]), ','.join(["'%s'" % arg  for arg in args  ]))
#                 print sql2
                db_mysql_cursor.execute(sql2 )   #插入数据到DB
                db_mysql_cursor.execute('commit') 
#                 db.insert('interface_case', **returnData[i])
    clear(db_mysql_conn)
    return returnData




path = DefaultConfig().data_path
print 'path0--->',path
# path = r'D:\workspace\web_autotest_my\src\data'
# print 'path--->',path
xls_list=testcasedata_xls_old_new.GetFileList('xlsx',path) + testcasedata_xls_old_new.GetFileList('xls',path)
print 'xls_list--->',xls_list

fail_num=[0] * len(xls_list)
pass_num=[0] *len(xls_list)

a = time.strftime("%H:%M:%S", time.localtime())
print '开始时间：', a
a1 = time.time()
for i in range(len(xls_list)):
    storedlist={}
    file_name=xls_list[i].split('/')[-1].split('_')[-1]
    storedlist=create_dict_db(xls_list[i])
#     print 'storedlist--->',storedlist


b = time.strftime("%H:%M:%S", time.localtime())
b1 = time.time()
print '结束时间：', b
print '共耗时：%s分 %s秒' % (int(b1 - a1)//60,int(b1-a1)%60)

# # 释放数据库连接资源
# global_config.clear()
