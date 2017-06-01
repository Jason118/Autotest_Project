# -*- coding: utf-8 -*-
"""文件上传类。用来实现页面的文件上传功能。

有三种上传方式：

    - <input>标签可以直接send_keys上传。
    - 或者打开窗口，通过win32gui获取句柄，实现上传功能。
    - 第三种方式是通过autoit工具生成的exe，通过命令行调用传参，实现上传。

class:

FileUpload -- file upload.

    methods:

        __init__(element)
            传入已经定位的upload按钮元素。

        upload_by_input(files)
            通过input标签的方法上传，直接send_keys。

        upload_by_win32(files, window_name=u'文件上传')
            通过win32api进行上传，打开窗口，在文件框输入文件地址并确认。

        upload_by_autoit(files, window_name=u'文件上传')
            通过autoit工具生成的exe进行上传，在命令行中调用并传参。

        upload(files, window_name=u'文件上传', autoit=False)
            综合判断，如果标签是input，则用upload_by_input上传。
            如果标签不是input，默认用upload_by_win32上传。
            如果标签不是input，并传参autoit=True，则用upload_by_autoit上传。
"""
import win32gui
import win32con
import os
from time import sleep
from src.utils.utils_exception import UploadWindowNotOpenError, UploadFileError, UploadWindowOpenError
from src.utils.logger import Logger
from src.utils.config import DefaultConfig

AUTOITEXE = {'firefox': 'upfile_autoit_firefox.exe',
             'chrome': 'upfile_autoit_chrome.exe',
             'internet explorer': 'upfile_autoit_ie.exe'
             }


class FileUpload(object):

    def __init__(self, driver, element, window_name=None):
        self.logger = Logger(__name__).get_logger()
        self.driver = driver
        self.Element = element
        self.window_open_flag = 0  # 用来标识窗口是否打开

        if window_name is not None:
            self.window_name = window_name
        elif self.driver.name == 'firefox':
            self.window_name = u'文件上传'
        elif self.driver.name == 'chrome':
            self.window_name = u'打开'
        elif self.driver.name == 'internet explorer':
            self.window_name = u'选择要加载的文件'

    def _files(self, files):
        """将files组织成可输入上传文件Edit框的类型

        如果传入的是str类型，则不需要组织。
        如果传入的是list列表，则需要组织成Edit框接受的格式。（主要是应对多文件上传）
        """
        self.files = ''
        if type(files) == list:
            for f in files:
                self.files += '"{0}" '.format(f)
        elif type(files) == str:
            self.files = files

    def _window_open(self):
        """判断窗口标识，如果未打开窗口，则打开上传窗口。"""
        if self.window_open_flag == 0:
            try:
                self.Element.click()
            except:
                raise UploadWindowOpenError('打开文件上传窗口失败！')
            sleep(1)

    # 三种方式上传
    def upload_by_input(self, files):
        """<input>标签直接send_keys即可。"""
        self._files(files)
        self.logger.info('upload {} by send_keys'.format(self.files))
        self.Element.send_keys(self.files)

    def upload_by_win32(self, files):
        """win32方式 —— 打开窗口，并上传文件。（支持多文件上传，files参数传入list）"""
        self._window_open()
        self._files(files)
        self.logger.info('upload {0} by win32'.format(self.files))

        upload = win32gui.FindWindow('#32770', self.window_name)

        # find Edit
        ComboBoxEx32 = win32gui.FindWindowEx(upload, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)

        # find confirm button
        button = win32gui.FindWindowEx(upload, 0, 'Button', None)

        # 验证是否打开窗口
        if upload and Edit and button:
            self.window_open_flag = 1
        else:
            raise UploadWindowNotOpenError('未发现上传文件对话框！')

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, self.files)
        win32gui.SendMessage(upload, win32con.WM_COMMAND, 1, button)

        self.window_open_flag = 0

    def upload_by_autoit(self, files):
        """autoit方式 —— 打开窗口，并上传文件（支持多文件上传，files参数传入list）"""
        self._window_open()
        self._files(files)
        self.logger.info('upload {} by autoit'.format(self.files))

        # 验证是否打开窗口
        if win32gui.FindWindow('#32770', self.window_name):
            self.window_open_flag = 1
        else:
            raise UploadWindowNotOpenError('未发现上传文件对话框！')

        upfile = os.path.abspath(DefaultConfig().base_path + '\\src\\resource\\' + AUTOITEXE[self.driver.name])
        os.system('{0} {1}'.format(upfile, self.files))  # 调用exe，上传文件

        self.window_open_flag = 0

    # 统一上传方式
    def upload(self, files, autoit=False):
        """综合判断，如果为<input>标签，则直接上传。否则默认用win32方式，如果传入autoit=True，则用autoit上传。"""
        if self.Element.tag_name == 'input' and type(files) != list:
            self.logger.info('it is a <input> tag.')
            self.upload_by_input(files)
        elif not autoit:
            self.upload_by_win32(files)
        else:
            self.upload_by_autoit(files)


if __name__ == '__main__':
    from selenium import webdriver
    from browser import Page
    # driver = webdriver.Firefox()
    driver = Page(url='http://www.sucaijiayuan.com/api/demo.php?url=/demo/20150128-1', browser='chrome')
    # driver.get('http://sahitest.com/demo/php/fileUpload.htm')
    # print driver.log_types
    # print driver.get_log('browser')
    # print driver.get_log('driver')
    driver.switch_to_frame('iframe')
    File = FileUpload(driver=driver, element=driver.find_element_by_class_name('filePicker'))
    # File.upload_by_input('d:\\baidu.py')
    File.upload_by_win32('d:\\baidu.py')
    File.upload_by_autoit(['d:\\1.html', 'd:\\baidu.py'])

    File.upload('d:\\1.html')
    # print driver.find_element_by_id('file').get_attribute('value')
    # for log in driver.get_log('browser'):
    #     print log
    # File.logger.info(driver.get_log('browser'))
    sleep(1)
    driver.quit()

