#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 14:08
# @Author  : Terry
import unittest

import time
from test.UI_test.page.HomePage import HomePage
from utils.getdb import db_sql_dict, db_mysql_connect, unicode_dict
from utils.reporter.HTMLTestRunner import HTMLTestRunner


class TestGcdtPageLogin(unittest.TestCase):
    def setUp(self):
        self.page_home = HomePage("ff")
        self.page_gcdt = self.page_home.gotoGcdtPage()

    def tearDown(self):
        self.page_gcdt.quit()

    def test_gcdtpage_normal_login(self):
        """
        测试购彩大厅页面【正常】登陆流程
        :return: 
        """
        str_sql = "select * from web_autotest_case where caseID like 'CP_WEB_PGHEADER_LOGIN%' and normal = 'Y' ;"
        lis_res = db_sql_dict(db_mysql_connect(), str_sql)
        for i in range(len(lis_res)):
            dic_test_data = unicode_dict(lis_res[i]["caseData"])
            str_username = unicode(dic_test_data["lg_username"])
            str_password = unicode(dic_test_data["lg_pwd"])
            str_expected_acc = unicode(dic_test_data["acc"])
            str_actual_acc = self.page_gcdt.loginNormal(str_username, str_password)
            self.assertEqual(str_expected_acc, str_actual_acc, "\n\nCASEID:\t%s\nExpect:\t%s\nActual:\t%s" % (lis_res[i]["caseID"], str_expected_acc, str_actual_acc))
            self.page_gcdt.logoutAndClose()
            self.page_home.gotoGcdtPage()

    def test_gcdtpage_abnormal_login(self):
        """
        测试购彩大厅页面【异常】登陆流程
        :return: 
        """
        str_sql = "select * from web_autotest_case where caseID like 'CP_WEB_PGHEADER_LOGIN%' and normal = 'N' ;"
        lis_res = db_sql_dict(db_mysql_connect(), str_sql)
        for i in range(len(lis_res)):
            dic_test_data = unicode_dict(lis_res[i]["caseData"])
            str_username = unicode(dic_test_data["lg_username"])
            str_password = unicode(dic_test_data["lg_pwd"])
            str_expected_pop = unicode(dic_test_data["popupmessage"])
            str_actual_pop = self.page_gcdt.loginAbnormal(str_username, str_password)
            self.assertEqual(str_expected_pop, str_actual_pop, "\n\nCASEID:\t%s\nExpect:\t%s\nActual:\t%s" % (lis_res[i]["caseID"], str_expected_pop, str_actual_pop))

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestGcdtPageLogin("test_gcdtpage_normal_login"))
    suite.addTest(TestGcdtPageLogin("test_gcdtpage_abnormal_login"))
    now = time.strftime("%Y%m%d", time.localtime(time.time()))
    fp = open("automate_report_%s.html" % now, mode="wb")
    runner = HTMLTestRunner(stream=fp,
                            verbosity=2,
                            title="test report",
                            description="test content")
    runner.run(suite)
