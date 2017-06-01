#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/31 9:32
# @Author  : Terry
import unittest

import time

from test.UI_test.common.string import update
from test.UI_test.page.BasePage import BasePage
from test.UI_test.page.HomePage import HomePage
from test.UI_test.page.PK10.PK10_Q1_ZXFS_Page import PK10_Q1_ZXFS_Page
from utils.config import DefaultConfig_Project
from utils.getdb import db_sql_dict, db_mysql_connect, unicode_dict
from utils.reporter.HTMLTestRunner import HTMLTestRunner


class Test_PK10_Q1_ZXFS_PAGE(unittest.TestCase):
    def setUp(self):
        self.page_home = HomePage("ff")
        self.page_gcdt = self.page_home.gotoGcdtPage()

    def tearDown(self):
        self.page_gcdt.quit()

    def test_pk10_q1_zxfs_normal(self):
        str_sql = "select * from web_autotest_case where caseID like 'CP_WEB_PK10_Q1_ZXFS%' and normal = 'Y' ;"
        lis_res = db_sql_dict(db_mysql_connect(), str_sql)
        for i in range(len(lis_res)):
            # 玩法
            str_model = unicode(lis_res[i]["model"])
            str_model1 = unicode(lis_res[i]["model1"])
            str_model2 = unicode(lis_res[i]["model2"])

            # 断言数据
            dic_test_data = unicode_dict(lis_res[i]["caseData"])
            str_popup_message1 = unicode(dic_test_data["popupwindow1"])
            str_popup_message2 = unicode(dic_test_data["popupwindow2"])
            str_income_and_expenses = unicode(dic_test_data["收支情况"])
            str_deal_type = unicode(dic_test_data["交易类型"])
            str_total_deal_money = unicode(dic_test_data["交易金额"])
            str_each_money = unicode(dic_test_data["单注额"])
            str_total_bet_money = unicode(dic_test_data["下注总额"])
            str_game_type = unicode(dic_test_data["methodid"])

            # 投注数据
            str_bet_num = unicode(dic_test_data["codes"])
            lis_bet_num = str_bet_num.split("|")

            # 用户信息
            str_username = DefaultConfig_Project().user_name
            str_password = DefaultConfig_Project().pass_word
            str_authnum = DefaultConfig_Project().auth_num

            # 登录并投注
            self.page_gcdt.loginNormal(str_username, str_password, str_authnum)
            self.page_gcdt.gotoGame(str_model, str_model1, str_model2)
            self.page_pk10_q1_zxfs = PK10_Q1_ZXFS_Page(self.page_gcdt.getDriver())
            str_actual_popup_message1, str_actual_popup_message2 = \
                self.page_pk10_q1_zxfs.bet_normal(lis_bet_num, str_each_money)

            # 更新期待的弹窗信息
            str_popup_message1 = update(str_popup_message1, self.page_pk10_q1_zxfs.get_issue())

            # 弹窗消息断言
            self.assertEqual(str_popup_message1, str_actual_popup_message1,
                             "\n\nCASEID:\t%s\nExpect:\t%s\nActual:\t%s" %
                             (lis_res[i]["caseID"], str_popup_message1, str_actual_popup_message1))
            self.assertEqual(str_popup_message2, str_actual_popup_message2,
                             "\n\nCASEID:\t%s\nExpect:\t%s\nActual:\t%s" %
                             (lis_res[i]["caseID"], str_popup_message2, str_actual_popup_message2))

            # 检查投注记录

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test_PK10_Q1_ZXFS_PAGE("test_pk10_q1_zxfs_normal"))
    now = time.strftime("%Y%m%d", time.localtime(time.time()))
    fp = open("automate_report_%s.html" % now, mode="wb")
    runner = HTMLTestRunner(stream=fp,
                            verbosity=2,
                            title="test report",
                            description="test content")
    runner.run(suite)
