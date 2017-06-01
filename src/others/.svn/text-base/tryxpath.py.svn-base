# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('./test.html')

print driver.find_element_by_xpath("//div[@id='C']/../..").text

print driver.find_element_by_xpath("//div[@id='C']/parent::*/parent::div").text

driver.quit()