# -*- coding: utf-8 -*-

import time
import random
import string
import os
from src.utils.logger import Logger


# date and time
def save_time():
    """:return 可用于文件名的时间日期字符串"""
    return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))


def save_date():
    """:return 可用于文件名的日期字符串"""
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def get_newest_file_of_path(path):
    """
    :param path: 文件夹路径
    :return path中创建日期最新的一个文件的文件名
    """
#     print sorted([(x, os.path.getctime(os.path.join(path, x))) for x in os.listdir(path)
#                    if os.path.isfile(os.path.join(path, x)) and (x != '__init__.py') and (x !='__init__.pyc')], key=lambda i: i[1])
    return sorted([(x, os.path.getctime(os.path.join(path, x))) for x in os.listdir(path)
#                    if os.path.isfile(os.path.join(path, x)) and (x != '__init__.py') and (x !='__init__.pyc')], key=lambda i: i[1])[-1]
                   if os.path.isfile(os.path.join(path, x)) and ('__init__.py' not in x)], key=lambda i: i[1])[-1]   #'__init__.py', '__init__.pyc' 排除在外


# phone
PHONE_PRE = ['139', '138', '137', '136', '135', '134', '133', '132', '131', '130',
             '178', '177', '176', '172', '170',
             '189', '188', '187', '186', '185', '184', '183', '182', '181', '180',
             '159', '158', '157', '156', '155', '153', '152', '151', '150',
             '149', '147', '145'
             ]


# todo(396214358@qq.com): 手机号检查与生成
def random_phone_number():
    """随机产生手机号"""
    return random.choice(PHONE_PRE) + ''.join(random.choice('0123456789') for i in range(8))


# string
def random_string(length=1):
    """随机产生长度为length的字符串"""
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


def list_to_str(list_in):
    """将list拼接成str"""
    list_out = list()
    for i in list_in:
        list_out.append(str(i))
    return ''.join(list_out)


def random_number_str(length=1):
    """随机产生长度为length的数字串"""
    return ''.join(list_to_str([random.randint(0, 9) for i in range(length)]))

# todo(396214358@qq.com): 身份证号检查与生成


# organization code
class OrganizationCode(object):
    """组织机构代码证支持类。支持生成随机代组织码证以及验证组织机构代码证。"""

    ORGANIZATION_CODE_MAP = string.digits + string.ascii_uppercase
    WMap = [3, 7, 9, 10, 5, 8, 4, 2]

    def __init__(self, code=None):
        """可传入code进行验证，可不传code生成可用代码证"""
        self.logger = Logger(__name__).get_logger()

        if not code:
            self.code = self.get_an_organization_code()
        else:
            self.code = code
        # bref and check
        if '-' in self.code:
            self.bref, self.check = self.code.split('-')
        else:
            self.check = self.code[-1:]
            self.bref = self.code[:-1]

    def _get_c9(self):
        """获取组织机构代码证的最后一位验证码 —— c9"""
        # C9=11-MOD（∑Ci(i=1→8)×Wi,11）
        sum = 0
        for ind, i in enumerate(self.bref):
            ci = self.ORGANIZATION_CODE_MAP.index(i)
            wi = self.WMap[ind]
            sum += ci * wi

        c9 = 11 - (sum % 11)
        if c9 == 10:
            c9 = 'X'
        elif c9 == 11:
            c9 = '0'
        return str(c9)

    def get_an_organization_code(self):
        """生成机构代码证并返回"""
        self.bref = random_string(8).upper()
        c9 = self._get_c9()
        organization_code = '{0}-{1}'.format(self.bref, c9)
        self.logger.info('生成组织机构代码证 {0}'.format(organization_code))
        return organization_code

    def check_organization_code(self):
        """检查组织机构代码证是否正确，如果正确，返回True，否则返回False"""
        if len(self.bref) != 8 or len(self.check) != 1:
            self.logger.info('组织机构代码证错误!（本体或校验码长度不符合要求）')
            return False
        else:
            try:
                c9_right = self._get_c9()
                if self.check != c9_right:
                    self.logger.info('组织机构代码证错误!（校验码错误）')
                    return False
                else:
                    self.logger.info('验证通过，组织机构代码证格式正确！')
                    return True
            except ValueError:
                self.logger.info('组织机构代码证错误!(本体错误)')
                return False


if __name__ == '__main__':
    # print save_time()
    # print save_date()
    # print random_phone_number()
    # print random_string()
    # print random_string(8)
    # print random_number_str(18)

    rand_or = OrganizationCode()
    print rand_or.code
    print OrganizationCode('WV0X1KYT-X').check_organization_code()
    print OrganizationCode('WV0X1KYT-5').check_organization_code()
    print OrganizationCode('WV0X1KYT-50').check_organization_code()
    print OrganizationCode('WV0X1KY@-5').check_organization_code()
    print OrganizationCode('WV0X1KYTX').check_organization_code()