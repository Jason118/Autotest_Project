# -*- coding: utf-8 -*-

from src.test.UI_test.page.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class PageHeader(BasePage):
    
    username = ('name', 'username')
    password = ('name', 'passwd')
    authnum = ('id', 'authnum')
    loginButton = ('name', 'login')
    loginUsername = ('name', 'user_name')
    Loc_signup = ('xpath', '//*[@id="logxinxi"]/div/div/div[2]/input[2]')   #注册
    Loc_signup = ('id', 'reg_free')                                         #免费注册
#     
# #     def __init__(self, browser='firefox'):
# #         super(PageHeader, self).__init__(browser)
# 
# #     Loc_user_apply = (By.LINK_TEXT, '商家入驻')
# #     Loc_signup = (By.LINK_TEXT, '注册')
#     Loc_signup = ('xpath', '//*[@id="logxinxi"]/div/div/div[2]/input[2]')
#     Loc_signup = ('id', 'reg_free')
# #     Loc_signup = ('css', '#logxinxi > div > div > div:nth-child(2) > input.dr_anniu.reg_anniu')
#     Loc_signin = (By.LINK_TEXT, '登录')
#     Loc_usercenter_zhigou = (By.CSS_SELECTOR, 'li.my-zhigou div a')
#     Loc_usercenter_userinfo = (By.CSS_SELECTOR, 'ul.my-zhigou-menu>li:nth-child(1)>a')
#     Loc_usercenter_myorders = (By.CSS_SELECTOR, 'ul.my-zhigou-menu>li:nth-child(2)>a')
#     Loc_usercenter_myfavors = (By.CSS_SELECTOR, 'ul.my-zhigou-menu>li:nth-child(3)>a')
#     Loc_usercenter_message = (By.CSS_SELECTOR, 'ul.my-zhigou-menu>li:nth-child(4)>a')
#     Loc_logout = (By.LINK_TEXT, '退出')
#     Loc_cart = (By.CSS_SELECTOR, 'div.header-cart a')
#     Loc_merchantcenter = (By.LINK_TEXT, '商户中心')
#     Loc_servicecenter = (By.LINK_TEXT, '服务大厅')
# 
#     Loc_productlist_0 = (By.CSS_SELECTOR, 'div#navtab_0 a')
#     Loc_productlist_2 = (By.CSS_SELECTOR, 'div#navtab_2 a')
#     Loc_productlist_3 = (By.CSS_SELECTOR, 'div#navtab_3 a')
#     Loc_productlist_4 = (By.CSS_SELECTOR, 'div#navtab_4 a')
#     Loc_productlist_5 = (By.CSS_SELECTOR, 'div#navtab_5 a')
#     Loc_productlist_6 = (By.CSS_SELECTOR, 'div#navtab_6 a')
#     Loc_productlist_7 = (By.CSS_SELECTOR, 'div#navtab_7 a')
# 
#     Loc_search_dropdown_btn = (By.CSS_SELECTOR, 'button.btn.dropdown-toggle')
#     Loc_dropdown_type0 = (By.CSS_SELECTOR, 'ul.dropdown-menu>li:nth-child(1)>a')
#     Loc_dropdown_type1 = (By.CSS_SELECTOR, 'ul.dropdown-menu>li:nth-child(2)>a')
#     Loc_search_content = (By.ID, 'searchName')
#     Loc_search = (By.CSS_SELECTOR, 'div.input-group-addon.search-submit input')
# 
#     def apply(self):
#         self.find_element(*self.Loc_user_apply).click()
# 
#     def signup(self):
#         self.findElement(self.Loc_signup).click()
# #         self.find_element(*self.Loc_signup).click()
# 
#     def signin(self):
#         self.find_element(*self.Loc_signin).click()
# 
#     def usercenter_myzhigou(self):
#         self.find_element(*self.Loc_usercenter_zhigou).click()
# 
#     def show_menu(self):
#         self.move_to(self.find_element(*self.Loc_usercenter_zhigou))
# 
#     def usercenter_userinfo(self):
#         self.show_menu()
#         self.find_element(*self.Loc_usercenter_userinfo).click()
# 
#     def usercenter_myorders(self):
#         self.show_menu()
#         self.find_element(*self.Loc_usercenter_myorders).click()
# 
#     def usercenter_myfavors(self):
#         self.show_menu()
#         self.find_element(*self.Loc_usercenter_myfavors).click()
# 
#     def usercenter_message(self):
#         self.show_menu()
#         self.find_element(*self.Loc_usercenter_message).click()
# 
#     def logout(self):
#         self.show_menu()
#         self.find_element(*self.Loc_logout).click()
# 
#     def cart(self):
#         self.find_element(*self.Loc_cart).click()
# 
#     def merchantcenter(self):
#         self.find_element(*self.Loc_merchantcenter).click()
# 
#     def servicecenter(self):
#         self.find_element(*self.Loc_servicecenter).click()
# 
#     def productlist_0(self):
#         self.find_element(*self.Loc_productlist_0).click()
# 
#     def productlist_2(self):
#         self.find_element(*self.Loc_productlist_2).click()
# 
#     def productlist_3(self):
#         self.find_element(*self.Loc_productlist_3).click()
# 
#     def productlist_4(self):
#         self.find_element(*self.Loc_productlist_4).click()
# 
#     def productlist_5(self):
#         self.find_element(*self.Loc_productlist_5).click()
# 
#     def productlist_6(self):
#         self.find_element(*self.Loc_productlist_6).click()
# 
#     def productlist_7(self):
#         self.find_element(*self.Loc_productlist_7).click()
# 
#     def change_searchtype(self, searchtype):
#         self.find_element(*self.Loc_search_dropdown_btn).click()
#         if searchtype == 0:
#             self.find_element(*self.Loc_dropdown_type0).click()
#         elif searchtype == 1:
#             self.find_element(*self.Loc_dropdown_type1).click()
#         else:
#             pass
# 
#     def search(self, searchtype=0, content=''):
#         self.change_searchtype(searchtype)
#         self.find_element(*self.Loc_search_content).send_keys(content)
#         self.find_element(*self.Loc_search).click()


if __name__ == '__main__':
#     from src.test.UI_test.page.bak.page_signin import PageSignIn
#     s = PageSignIn(browser=1,url='http://192.168.7.228/signin')
#     s.signin(username='13919093367', password='qqqq1111')
#     m = PageHeader(s.get_driver())
#     # m.apply()
#     # m.usercenter_myzhigou()
#     # m.usercenter_userinfo()
#     # m.usercenter_myorders()
#     # m.usercenter_myfavors()
#     # m.cart()
#     # m.merchantcenter()
#     # m.servicecenter()
#     # m.productlist_2()
#     # m.productlist_3()
#     # m.productlist_4()
#     # m.productlist_5()
#     # m.productlist_6()
#     # m.productlist_7()
#     # m.productlist_0()
#     # m.change_searchtype(1)
#     m.search(searchtype=1, content=u'乌合')
#     m.wait(1)
#     m.quit()
    m1 = PageHeader()
    m1.open("http://lotf.jwoquxoc.com/")
    m1.signup()
    time.sleep(2)
    m1.quit()