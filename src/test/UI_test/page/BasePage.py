#!/usr/bin/env python
#coding:utf-8

#Created on 2017年3月23日
import time

__author__ = 'Jason'

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.utils.config import DefaultConfig_Project

class BasePage(object):
    """description of class"""
    
    # webdriver instance
    def __init__(self, browser='firefox'):
        '''
        initialize selenium webdriver, use firefox as default webdriver
        若browser是driver类型，则直接赋值给self.driver，否则进行浏览器类型判断，生成新的driver。
        '''
        if isinstance(browser, WebDriver):
            self.driver = browser
        else:
            if browser == 'firefox' or browser == 'ff':
                driver = webdriver.Firefox()
            elif browser == 'chrome':
                driver = webdriver.Chrome()
            elif browser == 'internet explorer' or browser == 'ie':
                driver = webdriver.Ie()
            elif browser == 'opera':
                driver = webdriver.Opera()
            elif browser == 'phantomjs':
                driver = webdriver.PhantomJS()
            elif browser == 'edge':
                driver = webdriver.Edge()
            try:
                self.driver = driver
            except Exception:
                raise NameError("Not Found %s browser, You can enter 'ie', 'ff', 'opera', 'phantomjs', 'edge' or 'chrome'." % browser)

    def getDriver(self):
        """
        返回浏览器driver。
        :return: 
        """
        return self.driver

    def waitElement(self, element, secs=3):
        '''
        Waiting for an element to display.

        Usage:
        self.waitElement(("name","username"),10)
        '''
        try:
            type1 = element[0]
            value1 = element[1]

            if type1.lower() == "id" or type1.lower() == "i":
                WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.ID, value1)))
            elif type1.lower() == "name" or type1.lower() == "n":
                WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.NAME, value1)))
            elif type1.lower() == "class" or type1.lower() == "c":
                WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.CLASS_NAME, value1)))
            elif type1.lower() == "link_text" or type1.lower() == "l":
                WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.LINK_TEXT, value1)))
            elif type1.lower() == "partial_link_text" or type1.lower() == "p":
                WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value1)))
            elif type1.lower() == "tag_name" or type1.lower() == 't':
                WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.TAG_NAME, value1)))                
            elif type1.lower() == "xpath" or type1.lower() == "x":
                WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.XPATH, value1)))
            elif type1.lower() == "css" or type1.lower() == "s":
                WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value1)))
            else:
                raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
        except Exception:
            raise ValueError("No such element found"+ str(element))

    def waitElementText(self, element, text, secs=3):
        '''
        Waiting for the text to be present in element.

        Usage:
        self.waitElementText(("name","username"),10)
        '''
        try:
            type1 = element[0]
            value1 = element[1]

            if type1.lower() in ["id","name","class","link_text","xpath","css"]:
                WebDriverWait(self.driver, secs).until(EC.text_to_be_present_in_element(element, text))
            else:
                raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
        except Exception:
#             print  "The Text:%s not found in the element:%s" % (text, str(element))    
            raise ValueError("The Text:%s not found in the element:%s" % (text, str(element)))    
#         finally:
#             self.driver.quit()
                
    def findElement(self, element):
        '''
        Find element
        element is a set with format (identifier type, value), e.g. ('id', 'username')
        Usage:
        self.findElement(element)
        '''
        try:
            type1 = element[0]
            value1 = element[1]
#             print 'type1,value1',type1,value1
            if type1.lower() == "id" or type1.lower() == "i":
                elem = self.driver.find_element_by_id(value1)
            elif type1.lower() == "name" or type1.lower() == "n":
                elem = self.driver.find_element_by_name(value1)
            elif type1.lower() == "class" or type1.lower() == "c":
                elem = self.driver.find_element_by_class_name(value1)
            elif type1.lower() == "link_text" or type1.lower() == "l":
#                 print 'lisi'
                elem = self.driver.find_element_by_link_text(value1)
            elif type1.lower() == "partial_link_text" or type1.lower() == "p":
                elem = self.driver.find_element_by_partial_link_text(value1)
            elif type1.lower() == "tag_name" or type1.lower() == 't':
                element = self.driver.find_element_by_tag_name(value1)                
            elif type1.lower() == "xpath" or type1.lower() == "x":
                elem = self.driver.find_element_by_xpath(value1)
            elif type1.lower() == "css" or type1.lower() == "s":
#                 print 'zhangsan'
                elem = self.driver.find_element_by_css_selector(value1)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found"+ str(element))
        return elem
    
    def findElements(self, element):
        '''
        Find elements
        element is a set with format (identifier type, value), e.g. ('id', 'username')
        Usage:
        self.findElement(element)
        '''
        try:
            type1 = element[0]
            value1 = element[1]
            if type1.lower() == "id" or type1.lower() == "i":
                elem = self.driver.find_elements_by_id(value1)
            elif type1.lower() == "name" or type1.lower() == "n":
                elem = self.driver.find_elements_by_name(value1)
            elif type1.lower() == "class" or type1.lower() == "c":
                elem = self.driver.find_elements_by_class_name(value1)
            elif type1.lower() == "link_text" or type1.lower() == "l":
                elem = self.driver.find_elements_by_link_text(value1)
            elif type1.lower() == "partial_link_text" or type1.lower() == "p":
                elem = self.driver.find_elements_by_partial_link_text(value1)
            elif type1.lower() == "tag_name" or type1.lower() == 't':
                element = self.driver.find_elements_by_tag_name(value1)                
            elif type1.lower() == "xpath" or type1.lower() == "x":
                elem = self.driver.find_elements_by_xpath(value1)
            elif type1.lower() == "css" or type1.lower() == "s":
                elem = self.driver.find_elements_by_css_selector(value1)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found"+ str(element))
        return elem        
    
    def open(self, url=None):
        '''
        Open web url
        Usage:
        self.open(url)
        '''
        self.driver.maximize_window()   #最大化窗口
        if url == None:
#             print 'okk'
            url = DefaultConfig_Project().base_url
#             print url
            self.driver.get(url)
        else:
            self.driver.get(url)

            
            #raise ValueError("please provide a base url")
    
    def type(self, element, text):
        '''
        Operation input box.
        Usage:
        self.type(element, text)
        '''
        self.waitElement(element)
        el = self.findElement(element)
        el.clear()
        el.send_keys(text)

    def clear(self, element):
        '''
        Operation input box.
        Usage:
        self.clear(element)
        '''
        self.waitElement(element)
        el = self.findElement(element)
        el.clear()        
    
    def enter(self, element):
        '''
        Keyboard: hit return
        Usage:
        self.enter(element)
        '''
        el = self.findElement(element)
        el.clear()
        el.send_keys(Keys.RETURN)
        
    def click(self, element):
        '''Click page element, like button, image, link, etc.'''
        self.waitElement(element)
        el = self.findElement(element)
        chain = ActionChains(self.driver)
        chain.move_to_element(el)
        chain.click()
        chain.perform()
        
    def submit(self, element):
        '''
        Submit the specified form.
        Usage:
        self.submit(element)
        '''
        self.waitElement(element)
        el = self.findElement(element)
        el.submit()        
        
    def quit(self):
        '''Quit webdriver'''
        self.driver.quit()
        
    def getAttribute(self, element, attribute):
        '''Get element attribute'''
        el = self.findElement(element)
        return el.get_attribute(attribute)
    
    def getText(self, element, sec = 1):
        '''Get text of a web element'''
        time.sleep(sec)
        el = self.findElement(element)
        return el.text 
    
    def getTitle(self):
        '''Get window title'''
        return self.driver.title
    
    def getCurrentUrl(self):
        '''Get current url'''
        return self.driver.current_url
    
    def getScreenshot(self, targetpath):
        '''Get current screenshot and save it to target path'''
        self.driver.get_screenshot_as_file(targetpath)
        
    def maximizeWindow(self):
        '''Maximize current browser window'''
        self.driver.maximize_window()
        
    def setWindow(self, wide, high):
        '''
        Set browser window wide and high.

        Usage:
        driver.setWindow(wide,high)
        '''
        self.driver.set_window_size(wide, high)
        
    def back(self):
        '''Goes one step backward in the browser history.'''
        self.driver.back()
    
    def forward(self):
        '''Goes one step forward in the browser history.'''
        self.driver.forward()
        
    def getWindowSize(self):
        '''Gets the width and height of the current window.'''
        return self.driver.get_window_size()
    
    def refresh(self):
        '''Refresh current page.'''
        self.driver.refresh()
#         self.driver.switch_to()
        
    def switch_to_window(self, window_name):
        """
        跳转到一个窗口。
        :param window_name: 指窗口的编号，从0开始计数。
        :return: 无返回值。
        """
        self.driver.switch_to_window(self.driver.window_handles[window_name])

    def switch_to_frame(self, element):
        """
        跳转到一个frame。
        :param element:element is a set with format (identifier type, value), e.g. ('id', 'username')
        :return: 无返回值。
        """
        self.waitElement(element)
        el = self.findElement(element)
        self.driver.switch_to.frame(el)

    def switch_to_parent_frame(self):
        """
        从子frame切回到父frame。
        :return: 无返回值。
        """
        self.driver.switch_to.parent_frame()

    def switch_to_default_frame(self):
        """
        切到frame中之后，我们便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档。
        :return: 无返回值。
        """
        self.driver.switch_to.default_content()

    def close_current_window(self):
        """
        关闭当前窗口。
        使用该方法后，会失去当前窗口的句柄，需要使用Basepage类的switch_to_window方法跳转到一个窗口，以获得当前窗口句柄。
        否则，将无法继续操作。
        :return: 
        """
        self.driver.close()
    
    def getDisplay(self, selector):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("i,el")
        """
        el = self.findElement(selector)
        return el.is_displayed()
        
    def isSelected(self, element):
        el = self.findElement(element)
        return el.is_selected()
  
        
if __name__ == "__main__":
    driver = BasePage("ff")
#     driver.open("http://500vip.hqu29zoq.com/")
#     driver.open("http://lotf.jwoquxoc.com/")
    driver.open()
    element = ('name','username')
    b = driver.findElement(("name","username"))
    driver.type(("name","username"),'jtest')
    driver.type(('name','passwd'),'j12345')
    driver.type(('id','authnum'),'1111')
    driver.click(('name','login'))
    time.sleep(2)
    driver.click(('xpath', '//*[@id="header_user"]/div/span[5]/a[6]'))
    time.sleep(3)
    driver.quit()
            
        
        
        
        