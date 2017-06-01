#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/31 13:27
# @Author  : Terry
from selenium.webdriver import ActionChains
from test.UI_test.page.BasePage import BasePage


class Bet(BasePage):

    dic_bet_num = {}

    def bet(self, tup_bet_selector, str_bet_num):
        el_bet_selector = self.findElement(tup_bet_selector)
        if str_bet_num in self.dic_bet_num.keys():
            el_bet_num = el_bet_selector.find_element_by_id(self.dic_bet_num[str_bet_num])
            chain = ActionChains(self.getDriver())
            chain.move_to_element(el_bet_num)
            chain.click()
            chain.perform()
        else:
            str_valid_num = ", ".join(self.dic_bet_num.keys())
            raise KeyError(u"\nInvalid key: %s\nValid keys are: %s" % (str_bet_num, str_valid_num))
