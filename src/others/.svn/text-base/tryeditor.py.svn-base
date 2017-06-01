# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
# driver = webdriver.Chrome(executable_path='D:\py\AutoTestFramework\drivers\chromedriver.exe')
# driver.get('http://www.sucaijiayuan.com/api/demo.php?url=/demo/%E5%9F%BA%E4%BA%8Ebootstrap%E7%9A%84%E8%BD%BB%E9%87%8F%E7%BA%A7jQuery%E6%96%87%E6%9C%AC%E7%BC%96%E8%BE%91%E5%99%A8%E6%8F%92%E4%BB%B6%20LineControl/index.html')
# driver.maximize_window()
# driver.switch_to.frame('iframe')
# driver.find_element_by_class_name('Editor-editor').send_keys('Hello world again!')
# sleep(2)
# print driver.find_element_by_class_name('Editor-editor').text

# driver.get('http://www.sucaijiayuan.com/api/demo.php?url=/demo/20150325-1')
# driver.maximize_window()
# driver.switch_to.frame('iframe')
# driver.find_element_by_id('message1').send_keys('Hello world!')
# print driver.find_element_by_id('message1').get_attribute('value')


driver.get('http://ueditor.baidu.com/website/examples/completeDemo.html')

driver.switch_to.frame('ueditor_0')
body_string = """Hello world again again!
Hello world again again!
Hello world again again!

Hello world again again!"""
driver.find_element_by_tag_name('body').send_keys(body_string)

print driver.find_element_by_tag_name('body').text
driver.quit()
