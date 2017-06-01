# -*- coding: utf-8
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

from src.utils import TOOLS_PATH
from src.utils import log

by_dict = {'id': By.ID, 'name': By.NAME, 'class': By.CLASS_NAME, 'xpath': By.XPATH, 'css': By.CSS_SELECTOR,
           'tag': By.TAG_NAME, 'linktext': By.LINK_TEXT, 'partlinktext': By.PARTIAL_LINK_TEXT
           }


class UnsupportBrowser(StandardError):
    pass


class UnknowError(StandardError):
    pass


def open_browser(browser='firefox', profile=None, *args, **kwargs):
    """打开浏览器，允许三种类型，firefox,chrome,IE,否则会抛出异常。
    默认火狐浏览器，火狐浏览器可以使用指定的配置文件"""
    if browser.lower() == 'firefox':
        if profile is None:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Firefox(profile)
    elif browser.lower() == 'chrome':
        driver = webdriver.Chrome(TOOLS_PATH + 'browsertools\\chromedriver.exe')
    elif browser.lower() == 'ie':
        driver = webdriver.Ie(TOOLS_PATH + 'browsertools\\IEDriverServer.exe')
    else:
        log(u'open browser {0}'.format(browser), 'failed : UnsupportBrowser')
        raise UnsupportBrowser(msg='不支持的浏览器类型')
    driver.maximize_window()
    driver.implicitly_wait(30)
    log(u'open browser {0}'.format(browser), 'success.', 'info')
    return driver


def get(driver, url, *args, **kwargs):
    """打开网址"""
    try:
        driver.get(url)
    except:
        log(u'open url: {0}'.format(url), 'failed : UnknowError')
        raise UnknowError(msg='未知错误')
    log(u'open url: {0}'.format(url), 'success.', 'info')
    return driver


def check(fun):
    """检查是否能够获取到元素，如果可以返回该元素，否则抛出异常"""
    def find(driver, by, value, *args, **kwargs):
        if by.lower() in by_dict.keys():
            try:
                element = driver.find_element(by_dict[by.lower()], value)
            except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException) as e:
                log(u'find by {0}: {1}'.format(by, value), e)
                raise e
            except Exception, e:
                print e
                log(u'find by {0}: {1}'.format(by, value), 'failed : UnkownError')
                raise UnknowError(msg='未知错误')
        else:
            log(u'find by {0}: {1}'.format(by, value), 'failed : InvalidSelectorException')
            raise InvalidSelectorException(msg='没有匹配的定位方式')
        fun(driver, by, value, *args, **kwargs)
        return driver
    return find


@ check
def click(driver, by, value, *args, **kwargs):
    driver.find_element(by_dict[by.lower()], value).click()
    log(u'click by {0}: {1}'.format(by, value), 'success.', 'info')


@ check
def send_keys(driver, by, value, text, *args, **kwargs):
    driver.find_element(by_dict[by.lower()], value).send_keys(text)
    log(u'send keys by {0}: {1}, text="{2}"'.format(by, value, text), 'success.', 'info')


@ check
def clear(driver, by, value, *args, **kwargs):
    driver.find_element(by_dict[by.lower()], value).clear()
    log(u'clear by {0}: {1}'.format(by, value), 'success.', 'info')


def wait(driver, t, *args, **kwargs):
    import time
    time.sleep(int(float(t)))
    return driver


def close(driver, *args, **kwargs):
    driver.close()
    log(u'close driver {0}'.format(driver), 'success.', 'info')


def quitdriver(driver, *args, **kwargs):
    driver.quit()
    log(u'quit driver {0}'.format(driver), 'success.', 'info')


if __name__ == '__main__':
    dr = open_browser()
    dd = 1
    get(dr, url='http://www.baidu.com')
    send_keys(dr, 'id', 'kw', 'python')
    clear(dr, 'id', 'kw')
    quitdriver(dr)