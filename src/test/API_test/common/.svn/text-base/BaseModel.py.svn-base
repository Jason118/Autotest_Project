# -*- coding: utf-8 -*-
import json

import requests

from src.utils import Config
from src.utils import Encrypt
from src.utils import ReadXML
from src.utils import log


class BaseModel:

    def _header(self):
        u"""创建session，修改header，参数为json格式"""
        session = requests.session()
        session.headers.update({'Content-Type': 'application/json'})
        return session

    def _signandpost(self, param, name):
        u"""签名并发送"""
        sig = Encrypt().sign(param)
        param['sign'] = sig
        params_json = json.dumps(param)
        # print params_json
        log(name, params_json, 'info')

        url = ReadXML(Config().get('data', 'url_xml')).get_url(name)
        return self._header().post(url, params_json).content
