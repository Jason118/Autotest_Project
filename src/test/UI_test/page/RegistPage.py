#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/27 9:55
# @Author  : Terry
import time
from src.test.UI_test.page.BasePage import BasePage
from src.test.UI_test.page.LoginPage import LoginPage
from src.utils.config import DefaultConfig_Project


class RegistPage(BasePage):
    # 注册页面的立即登录按钮
    tup_login = ('xpath', '/html/body/div[2]/div/div/div[1]/div/a')

    # login
    tup_username = ('xpath', '//*[@id="reg_form_1"]/ul/li[1]/div[2]/input[1]')
    tup_password = ('xpath', '//*[@id="reg_form_1"]/ul/li[2]/div[2]/input')
    tup_confirm_password = ('xpath', '//*[@id="reg_form_1"]/ul/li[3]/div[2]/input')
    tup_authnum_level1 = ('xpath', '//*[@id="reg_form_1"]/ul/li[4]/div[2]/div[1]')
    tup_authnum_level2 = ('xpath', '//*[@id="verify"]')
    tup_agree = ("name", "reg_checkbox")
    tup_regist_button = ('xpath', '//*[@id="btn-sub"]')
    tup_popup = ('xpath', '//*[@id="_alert_"]/div')
    tup_normal_submit = ('xpath', '//*[@id="_alert_"]/div/button')

    # 正常注册后的页面检查
    tup_login_username = ('xpath', '//*[@id="header_user"]/div/span[1]/a')

    # 异常注册后的页面检查
    tup_abnormal_popup_message = ('xpath', '//*[@id="_alert_"]/div/p')
    tup_abnormal_submit = ('xpath', '//*[@id="_alert_"]/div/button')

    # logout
    str_logout_url = DefaultConfig_Project().base_url + "index/logout.html"

    def gotoLoginPage(self):
        self.click(self.tup_login)
        return LoginPage(self.getDriver())

    def registNormal(self, str_username, str_password, str_confirm_password, str_authnum = "1111"):
        """
        正常注册时调用registNormal方法。
        :param str_username: 用户名。
        :param str_password: 密码。
        :param str_confirm_password:确认密码。 
        :param str_authnum: 验证码。
        :return: 返回值。返回页面显示的用户名。
        """
        self.waitElement(self.tup_username)
        self.type(self.tup_username, str_username)  # 开始注册
        self.type(self.tup_password, str_password)
        self.type(self.tup_confirm_password, str_confirm_password)
        self.click(self.tup_authnum_level1)
        self.waitElement(self.tup_authnum_level2)
        self.click(self.tup_authnum_level2)
        self.type(self.tup_authnum_level2, str_authnum)
        if not self.isSelected(self.tup_agree):
            self.click(self.tup_agree)
        self.click(self.tup_regist_button)
        self.waitElement(self.tup_popup)  # 等待注册成功弹窗
        if self.getDisplay(self.tup_normal_submit):
            self.click(self.tup_normal_submit)
        self.waitElement(self.tup_login_username)
        time.sleep(1)
        str_acc = self.getText(self.tup_login_username)  # 读取显示的用户名
        return str_acc

    def registAbnormal(self, str_username, str_password, str_confirm_password, str_authnum = "1111"):
        """
        异常注册时调用registAbnormal方法。
        :param str_username: 用户名。
        :param str_password: 密码。
        :param str_confirm_password:确认密码。 
        :param str_authnum: 验证码。
        :return: 返回值。返回提示信息。
        """
        self.waitElement(self.tup_username)
        self.type(self.tup_username, str_username)
        self.type(self.tup_password, str_password)
        self.type(self.tup_confirm_password, str_confirm_password)
        self.click(self.tup_authnum_level1)
        self.waitElement(self.tup_authnum_level2)
        self.click(self.tup_authnum_level2)
        self.type(self.tup_authnum_level2, str_authnum)
        if not self.isSelected(self.tup_agree):
            self.click(self.tup_agree)
        self.click(self.tup_regist_button)
        self.waitElement(self.tup_abnormal_popup_message)
        time.sleep(1)
        str_abnormal_popup_message = self.getText(self.tup_abnormal_popup_message)
        if self.getDisplay(self.tup_abnormal_submit):
            self.click(self.tup_abnormal_submit)
        return str_abnormal_popup_message

    def logout(self):
        self.open(self.str_logout_url)
