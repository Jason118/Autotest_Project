#!/usr/bin/env python
#coding:utf-8

#Created on 2017年4月24日
__author__ = 'Jason'

"""发送Email。

class:

Email  -- 发送Email给指定用户，可带附件，通常可用于发送测试报告等。

    methods:

        __init__  -- 初始化Email类，读取配置或输入，获得邮件标题、发件人、收件人、附件等

        send  -- 发送Email。

"""
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from getpass import getpass
from socket import gaierror, error

from src.utils.config import DefaultConfig
from src.utils.logger import Logger
from src.utils.utils_exception import NoOptionError


class Email:
    """Email类，读取配置中的基本配置，初始化要求title必填，message与文件路径可选"""

    def __init__(self, title, message=None, path=None, server=None, sender=None, password=None, receiver=None):
        """初始化Email

        :param title: 邮件标题，必填。
        :param message: 邮件正文，非必填。
        :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
        :param server: smtp服务器，如果为空，则读取config.ini中的[email]/server，非必填。
        :param sender: 发件人，如果为空，则读取config.ini中的[email]/from，非必填。
        :param password: 发件人密码，如果为空，则读取config.ini中的[email]/password，如果读取失败，则需手动输入密码，非必填。
        :param receiver: 收件人，如果为空，则读取config.ini中的[email]/to，多收件人用“；”隔开，非必填。
        """
        self.logger = Logger(__name__).get_logger()

        self.title = title
        self.message = message
        self.files = path

        self.msg = MIMEMultipart('related')

        cf = DefaultConfig()
        if server:
            self.server = server
        else:
            self.server = cf.get('email', 'server')

        if sender:
            self.sender = sender
        else:
            self.sender = cf.get('email', 'from')

        if receiver:
            self.receiver = receiver
        else:
            self.receiver = cf.get('email', 'to')

        if password:
            self.password = password
        else:
            try:
                self.password = cf.get('email', 'pass')
            except NoOptionError:
                self.password = getpass(prompt=u'未在config.ini中检测到password，请输入password： ')
        
        if self.files:
            f = open(self.files, "rb")
            self.mail_body = f.read()
            # 关闭测试结果的文件
            f.close()
            
                

    def _attach_file(self, att_file):
        """内部方法，将单个文件添加到附件列表中"""
        att = MIMEText(self.mail_body, _subtype='html',_charset='utf-8')
        att["Content-Type"] = 'application/octet-stream'
        filename = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % filename[-1]
        self.msg.attach(att)
        self.logger.info('attach file {}'.format(att_file))

    def send(self):
        """组织邮件内容并发送邮件。"""

        self.msg['Subject'] = Header(self.title, "utf-8") 
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        # 邮件正文
        if self.message == None and self.files !=None:
            self.msg.attach(MIMEText(self.mail_body, _subtype='html',_charset='utf-8'))
        elif self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)
#             smtp_server.ehlo()    
            smtp_server.starttls()    #针对gmail 邮件服务器  http://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
        except (gaierror and error) as e:
            self.logger.exception(u'发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)
        else:
            try:
#                 print self.sender,self.password,self.server
                smtp_server.login(self.sender, self.password)
            except smtplib.SMTPAuthenticationError as e:
                self.logger.exception(u'用户名密码验证失败！%s', e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())
            finally:
                smtp_server.quit()
                self.logger.info(u'发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                                 u'同时检查收件人地址是否正确'.format(self.title, self.receiver))

#     def send_email(self, file_name, receiver):
#         """
#         send mail
#         :param file_name:
#         :param receiver:
#         :return:
#         """
#         
#         # 打开测试报告结果
#         # r:read
#         # b:binary
#         f = open(file_name, "rb")
#         
#         # 将测试结果放到邮件的主体中
#         mail_body = f.read()
#         # 关闭测试结果的文件
#         f.close()
#         
#         # 声明一个邮件对象，用刚刚得到的邮件主体
# #         msg = MIMEText(mail_body, "html", "utf-8")
#         msg=MIMEMultipart()
#         
#         text = MIMEText(mail_body, _subtype='html',_charset='utf-8')
#         msg.attach(text)
# #         msg = email.mim
#         # 设置邮件的主题
#         msg["subject"] = Header("WEB自动化测试报告_%s" % file_name.split(".html")[0].split("web_autotest_report_")[1], "utf-8")   #获取时间
# 
#         #---这是附件部分---  
#         att = MIMEApplication(mail_body)  
#         att.add_header('Content-Disposition', 'attachment', filename=file_name)  
#         msg.attach(att)  
#         
#         # 创建一个SMTP服务对象
#         # simple message transfer protocol
#         # 简单的消息转移协议
#         smtpMail = smtplib.SMTP()
# 
#         # 连接SMTP的服务器
#         smtpMail.connect("smtp.gmail.com", 587)
#         smtpMail.starttls()  #针对gmail 邮件服务器  http://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
#         
#         emailFrom = "ddgmlxy@gmail.com"
#         password = "ddg123456"
#         smtpMail.login(emailFrom, password)
#         
#         # 使用SMTP的服务器发送邮件
#         smtpMail.sendmail(emailFrom, receiver, msg.as_string())
#         
#         # 退出SMTP对象
#         smtpMail.quit()

if __name__ == '__main__':
    tit = u'测试报告'
    tex = '这是今天的测试报告！请查看'
    p = DefaultConfig().get('path', 'report')
    from src.utils.support import get_newest_file_of_path
    newestfile = get_newest_file_of_path(p)
    print newestfile
    filename = p + newestfile[0]
    print filename
#     email = Email(title=tit, message=tex, path=[filename])
    email = Email(title=tit, path=filename)
    email.send()