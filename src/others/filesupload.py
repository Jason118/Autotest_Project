# -*- coding: utf-8 -*-

from selenium import webdriver
import win32gui
import win32con
import time

dr = webdriver.Firefox()
dr.get('http://www.sucaijiayuan.com/api/demo.php?url=/demo/20150128-1')

dr.switch_to.frame('iframe')
upload = dr.find_element_by_class_name('filePicker')
upload.click()
time.sleep(1)

# win32gui
dialog = win32gui.FindWindow('#32770', u'文件上传')
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)

button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, '"d:\\baidu.py" "d:\\upload.py" "d:\\1.html"')
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

print dialog
print Edit
print button

print dr.find_element_by_id('status_info').text
dr.quit()