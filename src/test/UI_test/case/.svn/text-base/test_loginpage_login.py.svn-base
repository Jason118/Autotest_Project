#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/26 13:33
# @Author  : Terry
import unittest

import time

from test.UI_test.page.HomePage import HomePage
from test.UI_test.page.LoginPage import LoginPage
from utils.getdb import db_sql_dict, db_mysql_connect, unicode_dict
from utils.reporter.HTMLTestRunner import HTMLTestRunner


class TestLoginPageLogin(unittest.TestCase):
    def setUp(self):
        self.page_home = HomePage(u"ff")
        self.page_regist = self.page_home.gotoRegistPage()
        self.page_login = self.page_regist.gotoLoginPage()

    def tearDown(self):
        self.page_login.quit()

    def test_loginpage_normal_login(self):
        str_sql = u"select * from web_autotest_case where caseID like 'CP_WEB_MAIN_LOGIN%' and normal = 'Y' ;"
        lis_res = db_sql_dict(db_mysql_connect(), str_sql)
        for i in range(len(lis_res)):
            dic_test_data = unicode_dict(lis_res[i][u"caseData"])
            str_username = unicode(dic_test_data[u"lg_username"])
            str_password = unicode(dic_test_data[u"lg_pwd"])
            str_expected_acc = unicode(dic_test_data[u"acc"])
            str_actual_acc = self.page_login.loginNormal(str_username, str_password)
            self.assertEqual(str_expected_acc, str_actual_acc, u"\n\nCASEID:\t%s\nExpect:\t%s\nActual:\t%s" % (lis_res[i][u"caseID"],str_expected_acc, str_actual_acc))
            self.page_login.logout()
            self.page_regist = self.page_home.gotoRegistPage()
            self.page_login = self.page_regist.gotoLoginPage()

    def test_loginpage_abnormal_login(self):
        str_sql = u"select * from web_autotest_case where caseID like 'CP_WEB_MAIN_LOGIN%' and normal = 'N' ;"
        lis_res = db_sql_dict(db_mysql_connect(), str_sql)
        for i in range(len(lis_res)):
            dic_test_data = unicode_dict(lis_res[i][u"caseData"])
            str_username = unicode(dic_test_data[u"lg_username"])
            str_password = unicode(dic_test_data[u"lg_pwd"])
            str_expected_pop = unicode(dic_test_data[u"popupmessage"])
            str_actual_pop = self.page_login.loginAbnormal(str_username, str_password)
            self.assertEqual(str_expected_pop, str_actual_pop, u"\n\nCASEID:\t%s\nExpect:\t%s\nActual:\t%s" % (lis_res[i][u"caseID"],str_expected_pop, str_actual_pop))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLoginPageLogin("test_loginpage_normal_login"))
    suite.addTest(TestLoginPageLogin("test_loginpage_abnormal_login"))
    now = time.strftime("%Y%m%d", time.localtime(time.time()))
    fp = open("automate_report_%s.html" % now, mode="wb")
    runner = HTMLTestRunner(stream=fp,
                            verbosity=2,
                            title="test report",
                            description="test content")
    runner.run(suite)
