#!/usr/bin/env python
#coding:utf-8

#Created on 2017年3月23日
__author__ = 'Jason'

from BasePage import BasePage

class GoogleMainPage(BasePage):
    """description of class"""
    searchbox = ('ID', 'lst-ib')
    
    def __init__(self, browser='firefox'):
        super(GoogleMainPage, self).__init__(browser)
        
    def inputSearchContent(self, searchContent):
        searchBox = self.findElements(self.searchbox)
        print 'aaa',searchBox
        self.type(searchBox[0], searchContent)
        self.enter(searchBox[0])
        

if __name__ == "__main__":
    a = GoogleMainPage()
    a.open("http://www.google.com")
    a.inputSearchContent("hao123")
    a.quit()