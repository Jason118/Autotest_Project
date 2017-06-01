#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/26 9:20
# @Author  : Terry
import time
from src.test.UI_test.page.BasePage import BasePage
from src.utils.config import DefaultConfig_Project


class LoginPage(BasePage):
    """
    先登录到网站首页，然后点击“注册”，在注册页面点击“立即登录”，跳转到登录页面。
    LoginPage类提供正常登录的方法loginNormal和异常登录的方法loginAbnormal。
    """
    # login
    tup_username = ("id", "username_login")
    tup_password = ("id", "passwd_login")
    tup_authnum_level1 = ('xpath', '//*[@id="_form_login"]/ul/li[3]/div[2]')
    # tup_authnum_level2 = ("name", "authnum")
    tup_authnum_level2 = ('xpath','//*[@id="_form_login"]/ul/li[3]/div[2]/input')
    tup_login_button = ("id", "btn-sub")
    tup_normal_submit = ('xpath', '//*[@id="_alert_"]/div/button')

    # 正常登录后页面检查
    tup_login_username = ("name", "user_name")

    #异常登录检查
    tup_abnormal_pop_message = ('xpath', '//*[@id="_alert_"]/div/p')
    tup_abnormal_submit = ('xpath', '//*[@id="_alert_"]/div/button')

    # logout
    str_logout_url = DefaultConfig_Project().base_url + "index/logout.html"
    # tup_logout = ('xpath', '//*[@id="header_user"]/div/span[5]/a[6]')

    def gotoLoginPage(self):
        """
        跳转到登录页面。
        :return: 
        """
        self.open()
        self.click(self.tup_regist)
        self.waitElement(self.tup_login)
        self.click(self.tup_login)

    def loginNormal(self, str_username, str_password, str_authnum="1111"):
        """
        正常登录时，调用loginNormal方法。
        :param str_username: 用户名。
        :param str_password: 密码。
        :param str_authnum: 验证码。
        :return: 返回值，返回正常登录后显示的用户名。
        """
        self.type(self.tup_username, str_username)
        self.type(self.tup_password, str_password)
        self.click(self.tup_authnum_level1)
        self.waitElement(self.tup_authnum_level2)
        self.click(self.tup_authnum_level2)
        self.type(self.tup_authnum_level2, str_authnum)
        self.click(self.tup_login_button)
        self.waitElement(self.tup_normal_submit)
        if self.getDisplay(self.tup_normal_submit):
            self.click(self.tup_normal_submit)
        self.waitElement(self.tup_login_username)
        time.sleep(1)
        str_acc = self.getText(self.tup_login_username)
        return str_acc

    def loginAbnormal(self, str_username, str_password, str_authnum = "1111"):
        """
        异常登录时，调用loginAbnormal方法。
        :param str_username: 用户名。
        :param str_password: 密码。
        :param str_authnum: 验证码。
        :return: 返回值，返回异常登录时的提示信息。
        """
        self.type(self.tup_username, str_username)
        self.type(self.tup_password, str_password)
        self.click(self.tup_authnum_level1)
        self.waitElement(self.tup_authnum_level2)
        self.type(self.tup_authnum_level2, str_authnum)
        self.click(self.tup_login_button)
        self.waitElement(self.tup_abnormal_pop_message)
        time.sleep(1)
        str_pop_message = self.getText(self.tup_abnormal_pop_message)
        if self.getDisplay(self.tup_abnormal_submit):
            self.click(self.tup_abnormal_submit)
        return str_pop_message

    def logout(self):
        """
        退出当前用户
        :return: 无返回值。
        """
        self.open(self.str_logout_url)

if __name__=='__main__':
    # 正常登录流程
    page_login = LoginPage("ff")
    page_login.gotoLoginPage()
    str_actual_acc = page_login.loginNormal("jtest", "j12345", "1111")
    print(str_actual_acc)
    page_login.logout()
    page_login.gotoLoginPage()
    str_actual_acc = page_login.loginNormal("jtest", "j12345", "1111")
    print(str_actual_acc)
    page_login.quit()

    # 异常登录流程
    page_login = LoginPage("ff")
    page_login.gotoLoginPage()
    str_actual_pop_message = page_login.loginAbnormal("jtest", "j1234", "1111")
    print str_actual_pop_message
    str_actual_pop_message = page_login.loginAbnormal("jtest", "j1234", "1111")
    print str_actual_pop_message
    page_login.quit()
