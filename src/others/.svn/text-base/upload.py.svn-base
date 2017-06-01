# -*- coding: utf-8 -*-
from selenium import webdriver
import win32gui
import SendKeys
import win32api
import win32con

dr = webdriver.Firefox()
dr.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = dr.find_element_by_id('file')


# send_keys
# upload.send_keys('d:\\baidu.py')
# print upload.get_attribute('value')


upload.click()
import time
time.sleep(1)

# win32gui
dialog = win32gui.FindWindow('#32770', None)
print 'dialog: %s' % dialog
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
print ComboBoxEx32
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
print 'combobox: %s' % ComboBox
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)

print 'Edit: %s' % Edit
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
print 'button: %s ' % button
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, 'd:\\baidu.py')
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)


# SendKeys
SendKeys.SendKeys('D:\\baidu.py')
SendKeys.SendKeys("{ENTER}")


# time.sleep(1)
print upload.get_attribute('value')
dr.quit()

