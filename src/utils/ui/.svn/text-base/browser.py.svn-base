# -*- coding: utf-8 -*-

import os
import time
from selenium import webdriver
from src.utils.config import DefaultConfig
from selenium.common.exceptions import WebDriverException
from src.utils.utils_exception import (
    UnSupportBrowserTypeException,
    ParameterError)
from src.utils.support import save_time, save_date
from selenium.webdriver.common.action_chains import ActionChains


# todo:log
# todo(396214358@qq.com): 完善Browser Page类，添加注释

DRIVER_PATH = DefaultConfig().driver_path
ChromeDriver = DRIVER_PATH + '\\chromedriver.exe'
IEDriver = DRIVER_PATH + '\\IEDriverServer.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': ChromeDriver, 'ie': IEDriver}


class Browser(object):
    """浏览器类，根据传入的参数打开不同的浏览器

    methods:

        __init__(url, browser_type='firefox')
            初始化浏览器。默认浏览器类型是firefox

        open()
            打开浏览器，打开url，并默认设置最大化窗口，设置隐性等待时间为30s

        save_screen_shot(name='screen_shot')
            保存屏幕截图。保存到report\{today date}\{date}-{time}_{name}.png下

        close()
            关闭当前window

        quit()
            退出浏览器
    """

    def __init__(self, url, browser_type='firefox'):
        self.type = browser_type.lower()
        self.current_url = url
        self._driver = self._check_type()
        if not self._driver:
            raise UnSupportBrowserTypeException('Only support Firefox, Chrome and IE!')

    def _check_type(self):
        if self.type in TYPES:
            return TYPES[self.type]
        else:
            return False

    def open(self):
        try:
            self.driver = self._driver(executable_path=EXECUTABLE_PATH[self.type])
        except WebDriverException:
            raise WebDriverException('打开浏览器出错，请检查浏览器驱动或版本兼容情况！')
        try:
            self.driver.get(self.current_url)
        except WebDriverException:
            self.driver.close()
            raise WebDriverException('打开网址出错，请检查网址或者网络！')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    @property
    def name(self):
        return self.driver.name

    def _png_name(self, name):
        day = save_date()
        tm = save_time()

        fp = DefaultConfig().report_path + day + "\\image"
        img_type = ".png"

        if not os.path.exists(fp):
            os.makedirs(fp)

        return str(fp) + "\\" + str(tm) + "_" + name + img_type

    def save_screen_shot(self, name='screen_shot'):
        image = self.driver.save_screenshot(self._png_name(name))
        return image

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


"""
class

Page
    base class of pages.

methods

    current_window
        return current window handle.
"""


class Page(Browser):
    def __init__(self, driver=None, browser='firefox', url=''):
        Browser.__init__(self, url=url, browser_type=browser)
        if not driver and not url:
            raise ParameterError('driver and url can\'t be null both.')
        elif not driver:
            self.open()
        else:
            self.driver = driver

    @property
    def current_window(self):
        return self.driver.current_window_handle

    def get_driver(self):
        return self.driver

    def wait(self, seconds=3):
        time.sleep(seconds)

    def execute(self, js):
        self.driver.execute_script(js)

    def move_to(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    # 以下8个方法寻找某个元素
    def find_element_by_id(self, value):
        return self.driver.find_element_by_id(value)

    def find_element_by_name(self, value):
        return self.driver.find_element_by_name(value)

    def find_element_by_class_name(self, value):
        return self.driver.find_element_by_class_name(value)

    def find_element_by_tag_name(self, value):
        return self.driver.find_element_by_tag_name(value)

    def find_element_by_link_text(self, value):
        return self.driver.find_element_by_link_text(value)

    def find_element_by_partial_link_text(self, value):
        return self.driver.find_element_by_partial_link_text(value)

    def find_element_by_css_selector(self, value):
        return self.driver.find_element_by_css_selector(value)

    def find_element_by_xpath(self, value):
        return self.driver.find_element_by_xpath(value)

    # 以下8个方法寻找一组元素，返回列表
    def find_elements_by_id(self, value):
        return self.driver.find_elements_by_id(value)

    def find_elements_by_name(self, value):
        return self.driver.find_elements_by_name(value)

    def find_elements_by_class_name(self, value):
        return self.driver.find_elements_by_class_name(value)

    def find_elements_by_tag_name(self, value):
        return self.driver.find_elements_by_tag_name(value)

    def find_elements_by_link_text(self, value):
        return self.driver.find_elements_by_link_text(value)

    def find_elements_by_partial_link_text(self, value):
        return self.driver.find_elements_by_partial_link_text(value)

    def find_elements_by_css_selector(self, value):
        return self.driver.find_elements_by_css_selector(value)

    def find_elements_by_xpath(self, value):
        return self.driver.find_elements_by_xpath(value)

    def switch_to_window(self, partial_url='', partial_title=''):
        """切换窗口
            如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
            如果窗口数>=3，则必须传入参数来确定要跳转到哪个窗口
        """
        all_windows = self.driver.window_handles
        flag = 0
        if len(all_windows) == 1:
            print 'only 1 window!'
        elif len(all_windows) == 2:
            other_window = all_windows[1-all_windows.index(self.current_window)]
            self.driver.switch_to.window(other_window)
            flag = 1
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if not partial_url and not partial_title:
                    raise ParameterError('窗口多于三个，请传入参数定位window！')
                elif partial_url and partial_title and partial_url in self.driver.current_url and partial_title in self.driver.title:
                    flag = 1
                    break
                elif not partial_title and partial_url in self.driver.current_url:
                    flag = 1
                    break
                elif not partial_url and partial_title in self.driver.title:
                    flag = 1
                    break
        if flag:
            print self.driver.current_url, self.driver.title
        else:
            raise ParameterError('并无匹配的窗口，请检查传入参数！')

    def switch_to_frame(self, param):
        self.driver.switch_to.frame(param)


if __name__ == '__main__':
    bd = 'https://www.baidu.com'
    dr = Page(url=bd, browser='ie')
    print dr.driver.name
    # dr.open()
    dr.find_element_by_id('kw').send_keys('python')
    dr.wait()
    dr.save_screen_shot()
    dr.quit()

