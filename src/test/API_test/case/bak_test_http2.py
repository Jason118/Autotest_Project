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

# db1=Global().get_db1_conn()
# # db1_cursor = db1.cursor()
# db2=Global().get_db2_conn()
# db2_cursor = db2.cursor()
# db_sqlserver_cursor = db_sqlserver_connect.cursor()

# aa = sql_query(db1,"select interfaceID,caseData,expResult from interface_case where interfaceID='CurBalance' ; ")
# aa = sql_query(db1,"select interfaceID,caseData,expResult from interface_case where interfaceID='CurBalance' or caseid like 'User_CanLogin_%' ; ")
aa = sql_query(db_mysql_connect(),"select interfaceID,caseData,expResult from interface_case  ; ")

print aa
bb = [{u'interfaceID': u'CurBalance', u'caseData': u'{"iUserKey":52235}'}, {u'interfaceID': u'CurBalance', u'caseData': u'{"iUserKey":99999}'}, {u'interfaceID': u'CurBalance', u'caseData': u'{"iUserKey":"jtest"}'}, {u'interfaceID': u'CurBalance', u'caseData': u'{"iUserKey":""}'}, {u'interfaceID': u'CurBalance', u'caseData': u'{}'}]

# 封装HTTP POST请求方法
@pytest.mark.parametrize("interfaceID,data,expResult",aa)
# @pytest.fixture(params=bb)
def test_post(interfaceID, data,expResult):
#         data = json.dumps(eval(data))
#         data = data.encode('utf-8')
    #url = 'CurBalance'
    url = 'http://' + str(DefaultConfig_Project().http_host) + ':' + str(DefaultConfig_Project().http_port) +'/'  + interfaceID + '/'
    # print 'urlnew',url
    if data !='':
        payload = ast.literal_eval(data)   #unicode dict to dict
        #payload = data
#             else:
#                 payload = {}

    payload["CurUserKey"] = CurUserKey
    payload["CurPassword"] = CurPassword
    payload["From"] = From
    payload["IP"] = IP


    src2 = ""
    #print 'payload.key',payload.keys()
    for key1 in sorted(payload.keys(),key=str.lower):  #按payload字典顺序排序，不区分大小写
        #print key1,payload[key1]
        src2 += str(payload[key1])
    src2=src2 + String_token
    #print src2,src2.decode('raw_unicode_escape')
    #token1=hashlib.md5(src2.decode('raw_unicode_escape')).hexdigest()
    token1 = hashlib.md5(src2).hexdigest()
    payload["Token"]=token1

    payload = json.dumps(payload)  #转化为json对象
    # print 'payload---->',payload

    response = requests.request('POST', url, data=payload)
    response = response.text
#             json_response = json.loads(response)
#     print 'json_response----', response.decode('raw_unicode_escape')

    #断言
    assert {} != json.loads(response.decode('raw_unicode_escape'))
    if 'SQL' in expResult:
        expResult = ast.literal_eval(expResult)
        expResult_list = sql_query_dict_one(db_sqlserver_connect(), expResult['SQL'])
        if "Records" in json.loads(response.decode('raw_unicode_escape')):
            for i in range(len(expResult_list)):

                # print 'ex_result:', expResult_list[i]
                # print 'act_result:', json.loads(response.decode('raw_unicode_escape'))['Records'][i]
                # assert set(expResult_list[i].items()).issubset(set(json.loads(response.decode('raw_unicode_escape'))['Records'][i].items()))
                # expResult_list[i].viewitems() <= json.loads(response.decode('raw_unicode_escape'))['Records'][i].viewitems()
                assert expResult_list[i].viewitems() <= json.loads(response.decode('raw_unicode_escape'))['Records'][i].viewitems()
                # assert expResult_list[i].items() <= json.loads(response.decode('raw_unicode_escape'))['Records'][i].items()
                # assert expResult_list[i] in json.loads(response.decode('raw_unicode_escape'))['Records'][i]
        else:
            for i in range(len(expResult_list)):
                # assert set(expResult_list[i].items()).issubset(set(json.loads(response.decode('raw_unicode_escape')).items()))
                assert expResult_list[i].viewitems() <= json.loads(response.decode('raw_unicode_escape')).viewitems()
                # assert expResult_list[i].items() <= json.loads(response.decode('raw_unicode_escape')).items()
                # assert expResult_list[i] in json.loads(response.decode('raw_unicode_escape'))
    else:
        # 断言
        assert response.decode('raw_unicode_escape')==expResult

