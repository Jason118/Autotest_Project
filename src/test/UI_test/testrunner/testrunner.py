#!/usr/bin/env python
#coding:utf-8
from src.utils.db2 import db_sqlserver_connect

#Created on 2017年4月24日
__author__ = 'Jason'

import csv 
import smtplib
import unittest

import time
from src.utils.reporter.HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication  

from src.utils.config import DefaultConfig
from src.utils.mail import Email
from src.utils.getdb import db_mysql_connect,db_sqlserver_connect,db_sql_dict,unicode_dict,clear



class TestRunner(object):
    def test_run(self):
#         self.db1_cursor = db_mysql_connect()
#         self.db2_cursor = db_sqlserver_connect()
        
        
        test_suite = unittest.TestSuite()
        
        
#         csv_file = open("./testrunner/test_case_with_header.csv", "r")
#         csv_data = csv.reader(csv_file)
#         
#         is_header = True
#         for row in csv_data:
#             if is_header:
#                 is_header = False
#                 continue
#             
#             if row[0] == "tc01":
#                 test_suite.addTest(RanzhiTestCase01(row[1]))
#             elif row[0] == "tc02":
#                 pass
# #                 test_suite.addTest(RanzhiTestCase02(row[1]))
#                 continue

        test_suite = self.creatTestSuite()
#         print ('test_suite-->',test_suite)


        now_time = time.strftime("%Y%m%d",time.localtime(time.time())) 
#         now_time = time.strftime("%Y%m%d_%H%M%S",time.localtime(time.time())) 
        file_name = DefaultConfig().report_path+"web_autotest_report_%s.html" % now_time
        report_file = open(file_name, "wb")
            
        html_test_runner = HTMLTestRunner(
            stream=report_file,
            title=u"WEB自动化测试报告_%s" % now_time,
            description=u"WEB自动化测试详情：")
            
        html_test_runner.run(test_suite)
#           
#   
        report_file.close()   
          
#         unittest.TextTestRunner().run(test_suite)  
         
#         self.send_email(file_name, "mlxyhr1@gmail.com")
#         print 'filename---->',file_name
#         print  file_name.split(".html")[0].split("web_autotest_report_")[1]
        Email(title=u"WEB自动化测试报告_%s" % file_name.split(".html")[0].split("web_autotest_report_")[1], path=file_name).send()
#         Email.send()
#         self.send_email(file_name, "zgsg18@163.com")
        
#         unittest.TextTestRunner().run(test_suite)  

        
    def creatTestSuite(self):
        test_suite=unittest.TestSuite()
        #定义测试文件查找的目录
    #     test_dir='E:\\test_project'
#         test_dir='../case'
        test_dir = DefaultConfig().base_path + '/src/test/UI_test/case/'
#         print test_dir
        #定义 discover 方法的参数
        discover=unittest.defaultTestLoader.discover(test_dir, pattern ='test*.py', top_level_dir=None)
        #discover 方法筛选出来的用例，循环添加到测试套件中
        for testSuite in discover:
            for testCase in testSuite:
                test_suite.addTests(testCase)
#         print test_suite
        return test_suite
        

            
        

if __name__ == "__main__":
    TestRunner().test_run()
#     file_name = "D:/workspace/web_autotest_my/src/report/web_autotest_report_20170424.html"
#     Email(title=u"WEB自动化测试报告_%s" % file_name.split(".html")[0].split("web_autotest_report_")[1], path=file_name).send()
    
 