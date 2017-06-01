# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

# from src.utils.config import DRIVER_PATH
driver = webdriver.Firefox()
# print DRIVER_PATH + 'chromedriver.exe'
# driver = webdriver.Chrome(DRIVER_PATH + 'chromedriver.exe')
# driver.implicitly_wait(10)
driver.get('http://zhidao.baidu.com')
# driver.set_page_load_timeout(2)
sleep(2)
driver.find_element_by_id('userbar-login').click()
# print driver.switch_to.active_element
sleep(2)
# print driver.switch_to.window(driver.window_handles[0])
# print driver.current_window_handle
# driver.find_element_by_id('passport-login-pop').click()
# if driver.find_element_by_name('userName').is_displayed():
#     print '1'
#     username = driver.find_element_by_name('userName')
#     username.click()
#     username.send_keys('xxx')
# else:
#     print '2'

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# WebDriverWait(driver, 0.5, 10).until(EC.presence_of_element_located(driver.find_element_by_name('userName')))
username = driver.find_element_by_name('userName')
# print username.location
username.click()
username.send_keys('xxx')
driver.create_web_element()
# driver.execute_script("document.getElment")

# driver.execute_script("document.getElementById('TANGRAM__PSP_8__userName').value='xxx'")

sleep(2)

driver.quit()