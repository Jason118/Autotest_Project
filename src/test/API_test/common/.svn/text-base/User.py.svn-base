# -*- coding: utf-8 -*-
import json

from tools.encrypt import Encrypt
from tools.logger import log

from BaseModel import BaseModel
from src.utils.randomGen import random_phone_number


class User(BaseModel):
    def __init__(self, mobile=None, username=None, password=None):
        u"""如果没有同时传入mobile,username和password，则随机生成，用户名与密码等于随机生成的手机号"""
        if mobile is None and username is None and password is None:
            r_phone = random_phone_number()
            self.mobile = self.username = self.password = r_phone
        elif password is not None and username is None and mobile is None:
            r_phone = random_phone_number()
            self.mobile = self.username = r_phone
            self.password = password
        else:
            self.mobile = mobile
            self.username = username
            self.password = password
        # 把初始化的用户信息打印出来以供阅读
        log(self.__repr__(), 'Init', 'info')
        print self

    def __repr__(self):
        return 'User<mobile={0}, username={1}, password={2}>'.format(self.mobile, self.username, self.password)

    def signup(self):
        u"""用户注册"""
        param = {
            "p_username": self.username,
            "p_mobile": self.mobile,
            "p_password": Encrypt().encrypt(self.password, 'SHA1')
        }

        response = self._signandpost(param, 'AddUser')
        log(response, 'Sign Up', 'info')
        return json.loads(response)['p_userid']


if __name__ == '__main__':
    u = User()
    print u.signup()
