#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/27 13:32
# @Author  : Terry
import unittest

import time
from test.UI_test.page.HomePage import HomePage
from utils.getdb import db_sql_dict, db_mysql_connect, unicode_dict, db_sqlserver_connect, db_sql_update
from utils.reporter.HTMLTestRunner import HTMLTestRunner


class TestRegistPageRegist(unittest.TestCase):
    def setUp(self):
        self.page_home = HomePage(u"ff")
        self.page_regist = self.page_home.gotoRegistPage()

    def tearDown(self):
        self.page_regist.quit()

    def check_user_exist(self, str_acc):
        """
        检查数据库中是否存在参数str_acc指定的用户。
        :param str_acc: 登录后，页面显示的用户名。
        :return: 若用户存在，则返回True；否则返回False。
        """
        str_sql_check_exist = u"SELECT * from tuser WHERE sUserid = '%s'" % str_acc
        lis_res = db_sql_dict(db_sqlserver_connect(), str_sql_check_exist)
        if 0 == len(lis_res):
            return False
        else:
            return True

    def clean_user(self, str_acc):
        """
        若用户已存在，则从数据库中删除该用户。
        :param str_acc: 登录后，显示的用户名。
        :return: 无返回值。
        """
        if self.check_user_exist(str_acc):
            str_sql_clean = u"DELETE from tuser WHERE sUserid = '%s'" % str_acc
            db_sql_update(db_sqlserver_connect(), str_sql_clean)

    def test_registpage_normal_regist(self):
        """
        测试注册页面【正常】注册流程
        :return: 无返回值。
        """
        str_sql = "select * from web_autotest_case where caseID like 'CP_WEB_USER_REGISTER%' AND normal = 'Y';"
        lis_res = db_sql_dict(db_mysql_connect(), str_sql)
        for i in range(len(lis_res)):
            dic_test_data = unicode_dict(lis_res[i]["caseData"])
            str_username = unicode(dic_test_data["reg_username"])
            str_password = unicode(dic_test_data["reg_pwd"])
            str_confirmed_password = unicode(dic_test_data["cfm_pwd"])
            str_expected_acc = unicode(dic_test_data["acc"])
            self.clean_user(str_expected_acc)
            str_actual_acc = self.page_regist.registNormal(str_username, str_password, str_confirmed_password)
            self.assertEqual(str_expected_acc, str_actual_acc,
                             "\n\nCASEID:\t%s\nExpect:\t%s\nActual:\t%s" % (lis_res[i]["caseID"], str_expected_acc, str_actual_acc))
            self.clean_user(str_expected_acc)
            self.page_regist.logout()
            self.page_regist = self.page_home.gotoRegistPage()

    def test_registpage_abnormal_regist(self):
        str_sql = "select * from web_autotest_case where caseID like 'CP_WEB_USER_REGISTER%' AND normal = 'N';"
        lis_res = db_sql_dict(db_mysql_connect(), str_sql)
        for i in range(len(lis_res)):
            dic_test_data = unicode_dict(lis_res[i]["caseData"])
            str_username = unicode(dic_test_data["reg_username"])
            str_password = unicode(dic_test_data["reg_pwd"])
            str_confirmed_password = unicode(dic_test_data["cfm_pwd"])
            str_expected_pop_message = unicode(dic_test_data["popupmessage"])
            str_actual_pop_message = self.page_regist.registAbnormal(str_username, str_password, str_confirmed_password)
            self.assertEqual(str_expected_pop_message, str_actual_pop_message,
                             "\n\nCASEID:\t%s\nExpect:\t%s\nActual:\t%s" %
                             (lis_res[i]["caseID"], str_expected_pop_message, str_actual_pop_message))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestRegistPageRegist(u"test_registpage_normal_regist"))
    suite.addTest(TestRegistPageRegist(u"test_registpage_abnormal_regist"))
    now = time.strftime("%Y%m%d", time.localtime(time.time()))
    fp = open("automate_report_%s.html" % now, mode="wb")
    runner = HTMLTestRunner(stream=fp,
                            verbosity=2,
                            title="test report",
                            description="test content")
    runner.run(suite)
