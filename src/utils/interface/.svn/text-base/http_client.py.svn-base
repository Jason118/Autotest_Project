# -*- coding: utf-8 -*-

import requests
import json
import ast
from src.utils.logger import Logger
from src.utils.utils_exception import UnSupportMethod
from src.utils.config import DefaultConfig_Project
from src.utils._cpkeywords import *

METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']


class HTTPClient(object):

    def __init__(self, url=None, method='POST', headers=None, cookie=None):
        """

        :param method:
        :param headers: Must be a dict. Such as headers={'Content_Type':'text/html'}
        """
        self.logger = Logger(__name__).get_logger()
        if url == None:
            self.url = 'http://' + str(DefaultConfig_Project().http_host) + ':' + str(DefaultConfig_Project().http_port) + '/'
        else:
            self.url = url
        self.session = requests.session()
        self.method = method.upper()
        self.headers = headers
        self.cookie = cookie

        self._set_header()
        self._set_cookie()

    def _set_header(self):
        """设置header"""
        if self.headers:
            self.session.headers.update(self.headers)
            self.logger.info('Set headers: {0}'.format(self.headers))

    def _set_cookie(self):
        """设置cookie"""
        if self.cookie:
            self.session.cookies.update(self.cookie)
            self.logger.info('Set cookies: {0}'.format(self.cookie))

    def _check_method(self):
        """检查传入的method是否可用。"""
        if self.method not in METHODS:
            self.logger.exception(UnSupportMethod(u'不支持的method:{0}，请检查传入参数！'.format(self.method)))
        else:
            return True

    def send(self, interfaceID, params=None, data=None, **kwargs):
        """send request to url.If response 200,return response, else return None."""
        if self._check_method():
            url = self.url + interfaceID + '/'
            try:
                if data != '' and isinstance(data,unicode):
                    payload = ast.literal_eval(data)  # unicode dict to dict
                else:
                    payload=data

                payload["CurUserKey"] = CurUserKey
                payload["CurPassword"] = CurPassword
                payload["From"] = From
                payload["IP"] = IP

                src2 = ""
                # print 'payload.key',payload.keys()
                for key1 in sorted(payload.keys(), key=str.lower):  # 按payload字典顺序排序，不区分大小写
                # print key1,payload[key1]
                    src2 += str(payload[key1])

                src2 = src2 + String_token
        # print src2,src2.decode('raw_unicode_escape')
        # token1=hashlib.md5(src2.decode('raw_unicode_escape')).hexdigest()
                token1 = hashlib.md5(src2).hexdigest()
                payload["Token"] = token1

                payload = json.dumps(payload)  # 转化为json对象
#                 print 'payload---->',payload

                # response = requests.request('POST', url=url, data=payload)
                response = requests.request(method=self.method, url=url, params=params, data=payload, **kwargs)
                response = response.text
        #             json_response = json.loads(response)
        #         print 'json_response----', response
                return response

            except Exception as e:
                self.logger.info('%s' % e)
                print 'eeee',e
                return {}
            # response = self.session.request(method=self.method, url=self.url, params=params, data=data, **kwargs)
            # self.logger.info('{0} {1}.'.format(self.method, self.url))
            # if response.status_code == 200:
            #     self.logger.info('request success: {0}\n{1}'.format(response, response.content.strip()))
            #     return response
            # else:
            #     self.logger.error('request failed: {0} {1}'.format(response, response.reason))


if __name__ == '__main__':
    sender = HTTPClient('http://www.baidu.com', 'get')
    res = sender.send()
    print res.status_code
    print res.content

