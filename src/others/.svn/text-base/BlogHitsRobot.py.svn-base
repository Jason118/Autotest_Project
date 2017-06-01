# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from threading import Thread
from src.utils.config import DefaultConfig
import random
driver_path = DefaultConfig().driver_path
KEYWORDS = [u'selenium 兼容 灰蓝', u'selenium 时间 灰蓝', u'selenium 文件上传 灰蓝', u'selenium 坑 灰蓝',
            u'selenium editor 灰蓝', u'selenium 结构设计 灰蓝', u'selenium ActionChains 灰蓝', u'selenium alert 灰蓝',
            u'selenium checkbox 灰蓝', u'selenium Select 灰蓝', u'selenium 网页内嵌 灰蓝', u'selenium 映射表 灰蓝',
            u'selenium 导航栏 灰蓝', u'selenium active_element 灰蓝', u'selenium close 灰蓝', u'selenium Keys 灰蓝',
            u'selenium 输出报告 示例 灰蓝', u'selenium autoit命令行 灰蓝']


def clk(driver, url):
    """locate and click url"""
    locator = (By.XPATH, '//span[contains(text(), "{0}")]/../../../../a'.format(url))
    try:
        WebDriverWait(driver, 5, 0.5).until(EC.element_to_be_clickable(locator))
        try:
            moved_to_element = driver.find_element_by_xpath('//span[contains(text(), "{0}")]'.format(url))
            target_element = driver.find_element(*locator)
            ActionChains(driver).move_to_element(to_element=moved_to_element).click(target_element).perform()
            sleep(1)
            if 'm.baidu.com' in driver.current_url:
                target_element.click()
            return 1
        except:
            return 0
    except TimeoutException:
        return 0


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def killphantomjs():
    os.system('taskkill /f /im phantomjs.exe')


def flush(browser, n):
    ua = DesiredCapabilities().IPHONE
    for i in range(n):
        if browser.lower() == 'firefox':
            driver = webdriver.Firefox()
        elif browser.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-extensions')
            driver = webdriver.Chrome(executable_path=driver_path + 'chromedriver.exe', chrome_options=options)
        elif browser.lower() == 'ie':
            driver = webdriver.Ie(executable_path=driver_path + 'IEDriverServer.exe')
        elif browser.lower() == 'phantomjs':
            killphantomjs()
            driver = webdriver.PhantomJS(executable_path=driver_path + 'phantomjs.exe', desired_capabilities=ua)
        driver.get('http://m.baidu.com')
        driver.find_element_by_id('index-kw').send_keys(random.choice(KEYWORDS), Keys.ENTER)
        clk(driver, url='csdn')
        sleep(1)
        print driver.find_element_by_class_name('article_t').text,
        print driver.find_element_by_xpath('//p[@class="date"]/i[2]').text
        driver.close()


if __name__ == '__main__':
    threads = []
    t1 = Thread(target=flush, args=('phantomjs', 100))
    threads.append(t1)
    t2 = Thread(target=flush, args=('phantomjs', 100))
    threads.append(t2)
    # t3 = Thread(target=flush, args=('phantomjs', 20))
    # threads.append(t3)
    # t4 = Thread(target=flush, args=('phantomjs', 20))
    # threads.append(t4)

    for t in threads:
        t.start()
        t.join()

    # killphantomjs()
