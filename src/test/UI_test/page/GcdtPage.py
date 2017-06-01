#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 9:58
# @Author  : Terry
from test.UI_test.page.BasePage import BasePage
from utils.config import DefaultConfig_Project
import time


class GcdtPage(BasePage):
    """
    先登录网站首页，点击购彩大厅，跳转到购彩大厅登陆页面
    GcdtPage类提供正常登陆的方法loginNormal和异常登陆的方法loginAbnormal。
    """
    # login
    tup_username = ("name", "username")
    tup_password = ("name", "passwd")
    tup_authnum_level1 = ("name", "div_top_click")
    tup_authnum_level2 = ("name", "authnum")
    tup_login_button = ("name", "login")

    # 正常登陆后页面检查
    tup_login_username = ("name", "user_name")

    # 异常登陆检查
    tup_pop_message = ('xpath', '//*[@id="_alert_"]/div/p')
    tup_abnormal_submit = ('xpath', '//*[@id="_alert_"]/div/button')

    # logout
    str_logout_url = DefaultConfig_Project().base_url + "index/logout.html"

    # 跳转到某个彩种
    tup_iframe1 = ("id", "iframe1")
    tup_iframe2 = ("css", "iframe#iframe2")
    dic_model = {
        u"PK10": {
            "locator": ("css", "#lot9 > div > div.lott-top > div.lott-name > a > img"),
            "model1": {
                u"前一": {
                    "locator": ("css", "#tabbar-div-s2 > span.tab-front > span.content"),
                    "model2": {}
                }
            }
        },
        u"重庆时时彩":{}
    }

    def _gotoHomePage(self):
        """
        跳转到网站首页
        :return: 无返回值。
        """
        self.switch_to_window(0)

    def loginNormal(self, str_username, str_password, str_authnum="1111"):
        """
        测试正常登陆时，调用loginNormal方法
        :param str_username: 用户名
        :param str_password: 密码
        :param str_authnum: 验证码
        :return: 返回值，返回正常登陆后显示的用户名
        """
        self.type(self.tup_username, str_username)
        self.click(self.tup_password)  # 增加一个点击操作，否则无法输入密码
        self.type(self.tup_password, str_password)
        self.click(self.tup_authnum_level1)  # 需要先点击验证码区域，才会显示验证码，才能输入验证码
        self.waitElement(self.tup_authnum_level2)
        self.type(self.tup_authnum_level2, str_authnum)
        self.click(self.tup_login_button)
        self.waitElement(self.tup_login_username)
        time.sleep(1)
        str_acc = self.getText(self.tup_login_username)
        return str_acc

    def loginAbnormal(self, str_username, str_password, str_authnum="1111"):
        """
        测试异常登陆时，调用loginAbnormal方法
        :param str_username: 用户名
        :param str_password: 密码
        :param str_authnum: 验证码
        :return: 返回值，返回异常登陆后显示的提示信息
        """
        self.type(self.tup_username, str_username)
        self.click(self.tup_password)  # 增加一个点击操作，否则无法输入密码
        self.type(self.tup_password, str_password)
        try:
            self.click(self.tup_authnum_level1)  # 需要先点击验证码区域，才会显示验证码，才能输入验证码
        except Exception, e:
            print Exception, ":", e
        self.waitElement(self.tup_authnum_level2)
        self.type(self.tup_authnum_level2, str_authnum)
        self.click(self.tup_login_button)
        self.waitElement(self.tup_pop_message)
        time.sleep(1)
        str_pop_message = self.getText(self.tup_pop_message)
        if self.getDisplay(self.tup_abnormal_submit):
            self.click(self.tup_abnormal_submit)
        return str_pop_message

    def logoutAndClose(self):
        """
        退出当前用户时，调用logout方法。
        :return: 无返回值。
        """
        self.close_current_window()
        self._gotoHomePage()
        self.open(self.str_logout_url)

    def gotoGame(self, str_model, str_model1, str_model2):
        """
        前提条件：当前页面是购彩大厅页面。
        依据str_model、str_model1、str_model2指定的彩种、大玩法、小玩法，跳转到指定页面。
        :param str_model: 彩种。
        :param str_model1: 大玩法。
        :param str_model2: 小玩法。
        :return: 无返回值。
        """
        self._gotomodel(str_model)
        self._gotomodel1(str_model, str_model1)
        self._gotomodel2(str_model, str_model1, str_model2)

    def _gotomodel(self, str_model):
        str_model = unicode(str_model)
        if self.dic_model:
            if str_model in self.dic_model.keys():
                self.waitElement(self.tup_iframe1)
                self.switch_to_frame(self.tup_iframe1)
                str_model_locator = self.dic_model[str_model]["locator"]
                self.waitElement(str_model_locator)
                self.click(str_model_locator)
            else:
                raise ValueError("\nInvalid model: ", str_model)
        else:
            raise Exception("\nPlease check data self.dic_model, which should not be empty!")

    def _gotomodel1(self, str_model, str_model1):
        str_model = unicode(str_model)
        str_model1 = unicode(str_model1)
        if self.dic_model[str_model]["model1"]:
            if str_model1 in self.dic_model[str_model]["model1"].keys():
                self.switch_to_default_frame()
                self.waitElement(self.tup_iframe2)
                self.switch_to_frame(self.tup_iframe2)
                str_model1_locator = self.dic_model[str_model]["model1"][str_model1]["locator"]
                self.waitElement(str_model1_locator)
                self.click(str_model1_locator)
        else:
            raise Exception('\nPlease check data self.dic_model[str_model]["model1"], which should not be empty!')

    def _gotomodel2(self, str_model, str_model1, str_model2):
        str_model = unicode(str_model)
        str_model1 = unicode(str_model1)
        str_model2 = unicode(str_model2)
        if self.dic_model[str_model]["model1"][str_model1]["model2"]:
            if str_model2 in self.dic_model[str_model]["model1"][str_model1]["model2"].keys():
                str_model2_locator = self.dic_model[str_model]["model1"][str_model1]["model2"][str_model2]
                self.waitElement(str_model2_locator)
                self.click(str_model2_locator)
        else:
            print("\nThere is no model2! Expected:\nmodel:%s\nmodel1:%s\nmodel2:%s"
                  % (str_model, str_model1, str_model2))
