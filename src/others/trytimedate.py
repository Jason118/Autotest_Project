# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.sucaijiayuan.com/api/demo.php?url=/demo/20141108-1/')

driver.switch_to.frame('iframe')

# js = "document.getElementById('txtBeginDate').removeAttribute('readonly')"
# js = "$('input[id=txtBeginDate]').removeAttr('readonly')"
# js = "$('input[id=txtBeginDate]').attr('readonly',false)"
js = "$('input[id=txtBeginDate]').attr('readonly','')"

driver.execute_script(js)

driver.find_element_by_id('txtBeginDate').send_keys('2016-08-24')
sleep(2)
print driver.find_element_by_id('txtBeginDate').get_attribute('value')

driver.quit()
