#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/31 8:35
# @Author  : Terry
from test.UI_test.page.BasePage import BasePage
from test.UI_test.page.PK10.Widget import PK10Bet


class PK10_Q1_ZXFS_Page(PK10Bet):
    tup_frame = ("css", "#iframe2")
    tup_current_issue = ("css", "#current_issue")
    tup_bet_selector = ("css", "#lt_selector > div.gds")
    tup_each_money = ("css", "#lt_sel_times")
    tup_add_button = ("css", "#lt_sel_insert")
    tup_buy_button = ("css", "#lt_buy")
    tup_popup_message1 = ("css", ".mdl>table>tbody>tr>td>h4")
    tup_confirm_button = ("css", "#confirm_yes")
    tup_popup_message2 = ("css", "#JS_blockPage > div > table > tbody > tr:nth-child(1) > td")
    tup_finish_button = ("css", "#alert_close_button")

    def bet_normal(self, lis_bet_num, str_each_money, flo_return_water=0):
        """
        正常登陆时，调用bet_normal方法。
        :param lis_bet_num: 投注的号码。
        :param str_each_money: 单注金额。
        :param flo_return_water: 返水百分比。
        :return: 返回投注成功时的弹窗信息。
        """
        self.switch_to_default_frame()
        self.waitElement(self.tup_frame)
        self.switch_to_frame(self.tup_frame)
        for i in range(len(lis_bet_num)):
            self.bet(self.tup_bet_selector, lis_bet_num[i])
        self.type(self.tup_each_money, str_each_money)
        self.click(self.tup_add_button)
        self.click(self.tup_buy_button)
        self.waitElement(self.tup_popup_message1)
        str_popup_message1 = self.getText(self.tup_popup_message1)
        if self.getDisplay(self.tup_confirm_button):
            self.click(self.tup_confirm_button)
        str_popup_message2 = self.getText(self.tup_popup_message2)
        return str_popup_message1, str_popup_message2

    def get_issue(self):
        """
        读取当前的彩票期数，并返回。
        :return: 返回当前的彩票期数。
        """
        return self.getText(self.tup_current_issue)
