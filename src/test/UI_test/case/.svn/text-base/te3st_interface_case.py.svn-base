#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Jason'
# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

import time
from func._cpkeywords import *
import ast
import unittest,HTMLTestRunner
import re


# 测试用例(组)类
class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', test_data=None, http=None, db1_cursor=None, db2_cursor=None):
        a=super(ParametrizedTestCase, self).__init__(methodName)
        self.test_data = test_data
        self.http = http
        self.db1_cursor = db1_cursor
        self.db2_cursor = db2_cursor

class TestInterfaceCase(ParametrizedTestCase):
    def setUp(self):
       pass
 
    # 测试接口1
    def test_interfacePost(self):
        # 根据被测接口的实际情况，合理的添加HTTP头
        # header = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0'
        #    }
        # self.http.set_header(header)
#         response = self.http.get(self.test_data.request_url,  self.test_data.request_param)

        response = self.http.post(self.test_data.interfaceID, self.test_data.caseData)
#         print 'response99---',response.decode('raw_unicode_escape')
#         response = response.text  # {'ret': '\u53c2\u6570\u975e\u6cd52'}
#             print  response.decode('raw_unicode_escape')
        
        if {} == response:
            self.test_data.result = 'Error'
            try:
                # 更新结果表中的用例运行结果
                self.db1_cursor.execute('UPDATE test_result SET result = %s WHERE caseID = %s', (self.test_data.result, self.test_data.caseID))
                self.db1_cursor.execute('commit')
            except Exception as e:
                print('%s' % e)
                self.db1_cursor.execute('rollback')
            return    
        if 'SQL' in self.test_data.expResult:
            try:
                # 如果有需要，连接数据库，读取数据库相关值，用于和接口请求返回结果做比较
    #             self.db2_cursor.execute('SELECT user_id FROM 1dcq_user WHERE mobile = %s',(eval(self.test_data.request_param)['mobile'],))
    #             user_id = self.db2_cursor.fetchone()[0]
    #             self.db2_cursor.close()
                #sql_query_dict(conn,self.test_data.expResult['SQL'])
                expResult = ast.literal_eval(self.test_data.expResult)
#                 expResult = {'SQL':"select iType,fMoney,fBetNum,iGiveUp,iStatus,sRemark ,(convert(varchar(20),dCreate,120)) as dCreateTEXT , sCreator, sCreatorIP ,(convert(varchar(20),dModified,120)) as dModifiedTEXT ,sModifier,sModifierIP from TRegDiscount where iType = 2;"}
                expResult_list = sql_query_dict_one(self.db2_cursor,expResult['SQL'])
#                 print 'expResult_list--->',expResult_list
#                 print response.decode('raw_unicode_escape')
                for i in range(len(expResult_list)):
                    try:              
                        # 断言
                        self.assertDictContainsSubset(expResult_list[i],json.loads(response.decode('raw_unicode_escape')))
                        self.test_data.result = 'Pass'
                    except AssertionError as e:
                        print('%s' % e) 
                        self.test_data.result = 'Fail'
                        self.test_data.reason = '%s' % e # 记录失败原因       
                        print 'reason----->',self.test_data.reason                    
            except AssertionError as e:
                print('%s' % e) 
                self.test_data.result = 'Fail'
                self.test_data.reason = '%s' % e # 记录失败原因       
                print 'reason----->',self.test_data.reason
        else:
            try:
                # 断言
                self.assertEqual(response.decode('raw_unicode_escape'),self.test_data.expResult)
                self.test_data.result = 'Pass'
            except AssertionError as e:
                print('%s' % e) 
                self.test_data.result = 'Fail'
                self.test_data.reason = '%s' % e # 记录失败原因       
                print 'reason----->',self.test_data.reason
            
        # 更新结果表中的用例运行结果
        try:
            self.db1_cursor.execute("UPDATE test_result SET result = '%s' WHERE caseID = '%s'" % (self.test_data.result, self.test_data.caseID))
            self.db1_cursor.execute("UPDATE test_result SET reason = '%s' WHERE caseID = '%s'" % (self.test_data.reason.replace("'","\\'"), self.test_data.caseID))  #原因中有单引号，转义处理
            self.db1_cursor.execute('commit')
        except Exception as e:
            print('%s' % e)
            self.db1_cursor.execute('rollback')
           
    def tearDown(self):
        pass     
            
