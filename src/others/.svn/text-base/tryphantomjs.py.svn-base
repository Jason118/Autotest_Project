# -*- coding: utf-8 -*-

from selenium import webdriver
from src.utils.config import DefaultConfig


driver_path = DefaultConfig().driver_path

driver = webdriver.PhantomJS(executable_path=driver_path + 'phantomjs.exe')
driver.get('http://www.baidu.com')
print driver.find_element_by_id('cp').text