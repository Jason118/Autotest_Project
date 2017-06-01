#!/usr/bin/env python
#coding:utf-8

#Created on 2017年3月23日
from src.test.UI_test.page.GcdtPage import GcdtPage
from src.test.UI_test.page.RegistPage import RegistPage

__author__ = 'Jason'

from BasePage import BasePage
from src.utils.config import DefaultConfig_Project
import time 

class HomePage(BasePage):
    """description of class"""

    # 购彩大厅按钮
    tup_gcdt = ('xpath', '//*[@id="header_box"]/ul/li[2]/a')
    # 首页的注册按钮
    tup_regist = ('xpath', '//*[@id="logxinxi"]/div/div/div[2]/input[2]')
#     searchbox = ('ID', 'lst-ib')
    #login 
    username = ('name', 'username')
    password = ('name', 'passwd')
    authnum = ('name', 'authnum')
    loginButton = ('name', 'login')
    

    
    #logout
#     logout_plink = ('p', '退出')
    logout_link = ('p', u'退出')  #driver.find_element_by_link_text(u"退出").click()
    logout_url = DefaultConfig_Project().base_url + 'index/logOut.html'
    
    #正常登录后页面检查 
    loginUsername = ('name', 'user_name')
        
    # 异常登录弹出页面
    popMessage = ("x","//*[@id='_alert_']/div/p")
    popMessage = ('x','//*[@id="_alert_"]/div/p')
    abnormalSubmit = ('x', "//div[@id='_alert_']/div/button")
    
    def gotoGcdtPage(self):
        """
        跳转到购彩大厅页面
        :return: 返回购彩大厅页面实例。
        """
        self.open()
        self.waitElement(self.tup_gcdt)
        self.click(self.tup_gcdt)
        self.switch_to_window(1)  # 跳转到第一个弹出页面：购彩大厅页面。
        self.maximizeWindow()
        return GcdtPage(self.getDriver())

    def gotoRegistPage(self):
        """
        跳转到注册页面。
        :return: 返回注册页面实例。
        """
        self.open()
        self.waitElement(self.tup_regist)
        self.click(self.tup_regist)
        return RegistPage(self.getDriver())

    def loginNormal(self, user_name, pass_word, acc=None, auth_num=1111):
        result = -1
#         self.open("http://lotf.jwoquxoc.com/")
        self.type(self.username, user_name)
        self.type(self.password, pass_word)
        self.type(self.authnum, auth_num)
        if acc==None:
            acc=user_name
        self.click(self.loginButton)
        self.waitElementText(self.loginUsername, acc)
        result = 0
        return result
#         print self.getText(self.loginUsername)
#         print user_name
#         assert self.getText(self.loginUsername) == user_name
#         try:
#             assert self.getText(self.loginUsername) == user_name
#         except Exception:
#             raise ValueError("The loginUsername:%s not equal the user_name:%s" % (self.getText(self.loginUsername), user_name))

    def loginAbnormal(self, user_name, pass_word, popupmessage, auth_num=1111):
#         self.open("http://lotf.jwoquxoc.com/")
        self.type(self.username, user_name)
        self.type(self.password, pass_word)
        self.type(self.authnum, auth_num)
        self.click(self.loginButton)
        time.sleep(1)
#         self.click(('x',"//div[@id='_alert_']/div/button"))
    
        pop_message = self.getText(self.popMessage)

#             self.click(self.abnormalSubmit)
        
#         aaa = self.get_display(self.abnormalSubmit)
#         print 'ppp__>',aaa
        if self.getDisplay(self.abnormalSubmit) :
           self.click(self.abnormalSubmit)
#         time.sleep(2)
#         self.refresh()
        time.sleep(1)
        return pop_message
#         try:
#             driver.find_element.xxxxx
#             a=True
#         except:
#             a=false


#           
    def logout(self): 
#         self.click(self.logout_link)
#         time.sleep(2)
        self.open(self.logout_url)
#         self.click(self.logout_xpath)
        time.sleep(1)


if __name__ == "__main__":
#     a = HomePage()
# #     a.open("http://500vip.hqu29zoq.com/")
#     a.open("http://lotf.jwoquxoc.com/")
# #     a.type(a.username, 'jtest')
# #     a.type(a.password, 'j12345')
# #     a.type(a.authnum, '1111')
# #     a.click(a.loginButton)
# #     a.waitElementText(a.loginUsername, 'jtest')
# #     b=a.getText(a.loginUsername)
# #     print 'b-->',b
#     a.loginNormal('jtestssss', 'j12345')
    

#     a.quit()
#     print 'ok'
    a = HomePage()
#     a.open("http://500vip.hqu29zoq.com/")
#     a.open("http://lotf.jwoquxoc.com/")
    a.open()
#     a.type(a.username, 'jtest')
#     a.type(a.password, 'j12345')
#     a.type(a.authnum, '1111')
#     a.click(a.loginButton)
#     a.waitElementText(a.loginUsername, 'jtest')
#     b=a.getText(a.loginUsername)
#     print 'b-->',b
    a.loginNormal('jtest', 'j12345')
    print 'okkkkk'
    time.sleep(4)
    a.logout()
    time.sleep(4)
    print 'nooooo'
    a.quit()
    print 'ok'
    