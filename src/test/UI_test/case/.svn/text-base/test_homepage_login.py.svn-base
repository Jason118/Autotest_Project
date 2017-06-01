# -*- coding: utf-8 -*-
import unittest
import time

# from src.test.API_test.common.BaseCaseOperate import BaseCaseOperate
from src.test.UI_test.page.HomePage import HomePage
# from src.utils import ReadXML
from HTMLTestRunner import HTMLTestRunner
from src.utils.filereader.excel_reader import ExcelReader
from src.utils.getdb import db_mysql_connect,db_sql_dict,unicode_dict





# class ParametrizedTestCase(unittest.TestCase):
#     """ TestCase classes that want to be parametrized should
#         inherit from this class.
#     """
# #     def __init__(self, methodName='runTest', db1_cursor=None, db2_cursor=None):
#     def __init__(self, methodName,db1_cursor=None, db2_cursor=None):
#         super(ParametrizedTestCase, self).__init__(methodName)
# #         self.test_data = test_data
# #         self.http = http
#         self.db1_cursor = db1_cursor
#         self.db2_cursor = db2_cursor

class TestHomePageLogin(unittest.TestCase):

    def setUp(self):
        self.a = HomePage()
        self.a.open()
     
    def tearDown(self):
        self.a.quit()

    def t33est_homepage_login_by_xlsx(self):
        u"正常登录"
        loginNormal_data = ExcelReader("CP_WEB.ZCDL_JASON.xlsx","MASTERPG_LOGIN").data
        i = 0
        
        for i in range(4):
            result = -1
            lg_username = loginNormal_data[i][u'\u6d4b\u8bd5\u6570\u636e'].split("lg_username=")[1].split("\n")[0]
            lg_pwd = loginNormal_data[i][u'\u6d4b\u8bd5\u6570\u636e'].split("lg_pwd=")[1].split("\n")[0]
            acc = loginNormal_data[i][u'\u6d4b\u8bd5\u6570\u636e'].split("acc=")[1].split("\n")[0]
            print lg_username,lg_pwd
            result = self.a.loginNormal(lg_username, lg_pwd, acc=acc)
#             time.sleep(4)
            print 'result---->',result
            if result == 0 :
                self.a.logout()


    def test_homepage_login_by_db(self):
        u"正常登录"
#         db_mysql_cursor = db_mysql_connect.cursor()
        
        sql1 = "select * from web_autotest_case where caseID like 'CP_WEB_MASTERPG_LOGIN%' and normal = 'Y' ;"
        
        aa = db_sql_dict(db_mysql_connect(),sql1)
        
        for i in range(len(aa)):
            result = -1
            caseData = unicode_dict(aa[i]["caseData"])
            lg_username = caseData["lg_username"]
            lg_pwd = caseData["lg_pwd"]
            acc = caseData["acc"]
#             print lg_username,lg_pwd,acc
            result = self.a.loginNormal(lg_username, lg_pwd, acc=acc)
            if result == 0 :
                self.a.logout()

    def test_homepage_login_abnormal_by_db(self):
        u"异常登录"
#         db1_cursor = db_mysql_connect()
        
        sql1 = "select * from web_autotest_case where caseID like 'CP_WEB_MASTERPG_LOGIN%' and normal = 'N' ;"
        
        aa = db_sql_dict(db_mysql_connect(),sql1)
        
        for i in range(len(aa)):
            caseData = unicode_dict(aa[i]["caseData"])
            lg_username = caseData["lg_username"]
            lg_username = unicode(lg_username, errors='ignore')
            lg_pwd = caseData["lg_pwd"]
            popupmessage = caseData["popupmessage"]
#             print (lg_username,lg_pwd,popupmessage)
            actual_result = self.a.loginAbnormal(lg_username, lg_pwd, popupmessage)
#             print 'actual_result-->',actual_result
            self.assertEqual(popupmessage, actual_result, "异常登录 提示信息：检验错误！用例ID：" + aa[i]["caseID"]+"excpectResult: "+ popupmessage + "but the actual_result:" +actual_result)

#             if result == 0 :
#                 self.a.logout()
            


if __name__ == '__main__':
#     db1_cursor = db_mysql_conn
#     test_suite = unittest.TestSuite()
#     test_suite.addTest(TestHomePageLogin("test_homepage_login_by_db"))
#     print test_suite
#     unittest.TextTestRunner().run(test_suite)
#     runner.run(test_suite)
#     unittest.main()
#     db_mysql_conn1 = db_mysql_conn
     
    suite=unittest.TestSuite()
    #将测试用例加入到测试容器中
#     suite.addTest(TestHomePageLogin("test_homepage_login_by_db"))
    suite.addTest(TestHomePageLogin("test_homepage_login_by_db"))
#     suite.addTest(TestHomePageLogin("test_homepage_login_222"))
     
    now = time.strftime("%Y%m%d",time.localtime(time.time())) 
    fp = open("automate_report_%s.html" % now,mode="wb")
    runner = HTMLTestRunner(stream=fp,
                            verbosity=2,
                            title="test report",
                            description="test content")
    runner.run(suite)
    fp.close()
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    