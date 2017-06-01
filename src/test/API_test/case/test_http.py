#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Jason'

import requests
import json
import configparser
from src.utils._cpkeywords import *
import ast
import pytest
from src.utils.config import DefaultConfig_Project
from src.utils.getdb import db_mysql_connect, db_sqlserver_connect
from src.utils.interface.http_client import HTTPClient
from  unittest.case import TestCase 
from src.utils.assert_extra import assertDictContainsSubset


sql = "select interfaceID,caseData,expResult from interface_case;" 


# 封装HTTP POST请求方法
@pytest.mark.parametrize("interfaceID,data,expResult",sql_query(db_mysql_connect(),sql))
# @pytest.fixture(params=bb)
def test_post(interfaceID, data,expResult):
    response=HTTPClient().send(interfaceID,data=data)
    # print 'response',response

    #断言
    assert {} != json.loads(response.decode('raw_unicode_escape'))
    expResult = ast.literal_eval(expResult)
    if 'SQL' in expResult:
        expResult_list = sql_query_dict_one(db_sqlserver_connect(), expResult['SQL'])
        if "Records" in json.loads(response.decode('raw_unicode_escape')):
            for i in range(len(expResult_list)):

                # print 'ex_result:', expResult_list[i]
                # print 'act_result:', json.loads(response.decode('raw_unicode_escape'))['Records'][i]
                # assert set(expResult_list[i].items()).issubset(set(json.loads(response.decode('raw_unicode_escape'))['Records'][i].items()))
                assertDictContainsSubset(expResult_list[i], json.loads(response.decode('raw_unicode_escape'))['Records'][i],'haha1两者不匹配1：')
                # assert expResult_list[i].viewitems() <= json.loads(response.decode('raw_unicode_escape'))['Records'][i].viewitems()
        else:
            for i in range(len(expResult_list)):
                # assert set(expResult_list[i].items()).issubset(set(json.loads(response.decode('raw_unicode_escape')).items()))
                assertDictContainsSubset(expResult_list[i], json.loads(response.decode('raw_unicode_escape')),'haha2两者不匹配2：')
#                 assert expResult_list[i].viewitems() <= json.loads(response.decode('raw_unicode_escape')).viewitems()
    else:
        # 断言
#         TestCase().assertDictContainsSubset(expResult, json.loads(response.decode('raw_unicode_escape')))
        assertDictContainsSubset(expResult, json.loads(response.decode('raw_unicode_escape')), 'haha3两者不匹配3：')
#         assert expResult.viewitems() <= json.loads(response.decode('raw_unicode_escape')).viewitems()


if __name__ == '__main__':
    now_time = time.strftime("%Y%m%d", time.localtime(time.time()))
    args = ['-q', '-s', '--html=../../../../report/interface_autotest_report_%s.html' % now_time]
    pytest.main(args)