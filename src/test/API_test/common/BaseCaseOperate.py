# -*- coding: utf-8 -*-
import json

import requests
from src.utils.encrypt import Encrypt
from src.utils.logger import Logger
from src.utils.filereader.excel_reader import ExcelReader

from MerchantCenter import MerchantCenter
from OnlinePurchase import OnlinePurchase
from PersonalCenter import PersonalCenter
from src.utils.support import random_number_str


class BaseCaseOperate:

    def __init__(self, url, datafile='zhigou.xlsx', sheet_name='sheet0', ifsign=1, userid=None, prepare=False):
        self.url = url
        self.datafile = datafile
        self.sheet_name = sheet_name
        self.ifsign = ifsign
        self.userid = userid
        self.cases = ExcelReader(self.datafile, sheet_name=self.sheet_name).get_data()
        self.case = None
        self.types = self.cases.pop(0)

        self.on = OnlinePurchase(self.userid)
        self.pre = prepare

    def prepare(self):
        self.on.ReceiveaddrAdd()
        self.on.ShoppingCartAdd()
        self.on.ShoppingCartAdd(merchant=29, product=2, countnum=2, spectypegroup_id='6*7')
        self.on.ShoppingCartAdd(merchant=30, product=1, countnum=3, spectypegroup_id='10*11')

        self.on.PresettlementCreate()

    def _datatypeparse(self):
        u"""将读取到的参数列表的第一项，即excel中的第二行，解析为参数的type，把所有的参数按照这个对应的type做处理。
        1.将所有为‘null’的字段都解析为None
        2.将type为‘int’的字段强制转换成int类型
        3.将type为‘str’的字段直接赋值
        4.将type为‘password’的字段进行加密，zhigou的加密方式为SHA1
        5.将type为‘best’的字段，加上盐，与id拼接并加密，zhigou的方式为MD5
        处理完之后，返回处理后的参数列表"""
        if self.pre:
            try:
                self.prepare()
            except:
                print u'prepare()未正常执行'
        params = dict()
        mes = ''
        for key in self.types.keys():
            if self.case[key] == 'null':
                params[key] = None
                mes = mes + key + 'None'
            elif self.case[key] == 'userid':
                params[key] = self.userid
                mes = mes + key + str(self.userid)
            elif self.case[key] == 'addrid':
                params[key] = self.on.get_Receiveaddr_ids()[0]
            elif self.case[key] == 'shoppingid':
                params[key] = self.on.get_Shopping_ids()[0]
            elif self.case[key] == 'shoppingids':
                params[key] = self.on.list_to_str(self.on.get_Shopping_ids(), ';')
            elif self.case[key] == 'shoppingids,':
                params[key] = self.on.list_to_str(self.on.get_Shopping_ids(), ',')
            elif self.case[key] == 'prosettlementid':
                params[key] = self.on.prosettlementid
            elif self.case[key] == 'prosetparid':
                params[key] = self.on.list_to_str(self.on.get_prosetpar_ids(), ';')
            elif self.case[key] == 'attachlist':
                params[key] = self.on.get_attachlist()
            elif self.case[key] == 'attachlists':
                params[key] = self.on.get_attachlist() * 2
            elif self.case[key] == 'orderpageid':
                self.on.OrderAdd()
                params[key] = self.on.orderpageid
            elif self.case[key] == 'orderid':
                try:
                    self.on.OrderAdd()
                except:
                    pass
                # self.on.get_order_ids()
                params[key] = self.on.list_to_str(self.on.get_order_ids(), ',')
                # print params[key]
            elif self.case[key] == 'orderid_from_db':
                params[key] = self.on.get_order_id_from_db()
            elif self.case[key] == 'best+pass':
                from MerchantAdd import MerchantAdd
                params[key] = Encrypt(pwd_key='').encrypt('{0}111111'.format(MerchantAdd(self.userid).return_best_id()), 'MD5')
            elif self.case[key] == 'nickname':
                params[key] = 'nickname' + random_number_str(6)
            elif self.case[key] == '"null"':
                params[key] = 'null'
            elif self.case[key] == 'idcard':
                params[key] = random_number_str(18)
            elif self.case[key] == 'mobile':
                params[key] = PersonalCenter(userid=self.userid).getmobile()
            elif self.case[key] == 'pass':
                PersonalCenter(userid=self.userid).user_resetpassword('111111')
                params[key] = Encrypt().encrypt('111111', 'SHA1')
            elif self.case[key] == 'brandname':
                params[key] = '品牌{0}'.format(random_number_str(5))
            elif self.case[key] == 'brandid':
                MerchantCenter(userid=self.userid).add_brand(brandname='x1x', brandad='s.png', brandlogo='g.png', brandintr='')
                params[key] = MerchantCenter(userid=self.userid).get_brand_ids()[0][0]
            elif self.case[key] == 'levelid':
                try:
                    print MerchantCenter(userid=self.userid).add_custlist(levelname='add_and_delete', username='15876862305')
                except:
                    pass
                params[key] = MerchantCenter(userid=self.userid).get_username_from_db(levelname='add_and_delete')
            elif self.case[key] == 'randomproductname':
                params[key] = '云南普洱{0}'.format(random_number_str(5))
            elif self.case[key] == 'productid':
                m = MerchantCenter(userid=self.userid)
                params[key] = m.add_product_2(brand_id=m.get_brand_ids()[0][0])
            elif self.case[key] == 'addressid':
                s = MerchantCenter(self.userid)
                s.sendaddr_add(send_name='TestSendName', address='TestAddress', mobile='13622222222', location_id='110101')
                params[key] = s.get_send_address_id()
            elif self.case[key] == 'notprepareorder':
                params[key] = MerchantCenter(userid=self.userid).get_not_prepare_order_from_db()
            elif self.case[key] == 'notsendorder':
                buyer = OnlinePurchase(248)
                buyer.ShoppingCartAdd(merchant=1708, product=164, countnum=1, spectypegroup_id='112*114')
                buyer.PresettlementCreate()
                buyer.OrderAdd()
                buyer.Purchase_Pay()
                m = MerchantCenter(self.userid)
                m.prepare(order_id=m.get_not_prepare_order_from_db())
                params[key] = m.get_not_send_order_from_db()
            elif self.case[key] == 'orderlogistics':
                params[key] = MerchantCenter(self.userid).get_not_receive_order_from_db()
            elif self.case[key] == 'notpayorder':
                try:
                    params[key] = MerchantCenter(self.userid).get_not_pay_order_from_db()
                except:
                    buyer = OnlinePurchase(248)
                    buyer.ShoppingCartAdd(merchant=1708, product=164, countnum=1, spectypegroup_id='112*114')
                    buyer.PresettlementCreate()
                    buyer.OrderAdd()
                    params[key] = MerchantCenter(self.userid).get_not_pay_order_from_db()
            elif self.case[key] == 'userorderlogistics':
                params[key] = OnlinePurchase(self.userid).get_not_receive_order_from_db()
            elif self.case[key] == 'notreceiveorder':
                try:
                    params[key] = OnlinePurchase(self.userid).get_not_receive_order_from_db()
                except:
                    buyer = OnlinePurchase(self.userid)
                    buyer.ShoppingCartAdd(merchant=1708, product=164, countnum=1, spectypegroup_id='112*114')
                    buyer.PresettlementCreate()
                    buyer.OrderAdd()
                    m = MerchantCenter(self.userid)
                    m.prepare(order_id=m.get_not_prepare_order_from_db())
                    m.send(orderid=m.get_not_send_order_from_db(), send_id=123456789, logistics_id=9, send_address=8174, send_remarks='')
                    params[key] = buyer.get_not_receive_order_from_db()
            elif self.case[key] == 'personalnotprepareorder':
                params[key] = OnlinePurchase(userid=self.userid).get_not_prepare_order_from_db()

            elif self.types[key] in ['int', 'str', 'password', 'best', 'md5', 'double']:
                if self.types[key] == 'int':
                    try:
                        params[key] = int(self.case[key])
                    except ValueError:
                        params[key] = self.case[key]
                elif self.types[key] == 'double':
                    try:
                        params[key] = float(self.case[key])
                    except ValueError:
                        params[key] = self.case[key]
                elif self.types[key] == 'str':
                    params[key] = self.case[key]
                elif self.types[key] == 'password':
                    params[key] = Encrypt().encrypt(self.case[key], 'SHA1')
                elif self.types[key] == 'md5':
                    params[key] = Encrypt(pwd_key='').encrypt(self.case[key], 'MD5')
                elif self.types[key] == 'best':
                    try:
                        params[key] = Encrypt(pwd_key=self.case[key]).encrypt(self.case['BEST_user_id'], 'MD5')
                    except KeyError:
                        raise KeyError('Did not find key "BEST_user_id",check your data file!')
                # print key,params[key]
                try:
                    mes = mes + key + params[key].decode('utf-8')
                except AttributeError:
                    mes = mes + key + str(params[key])
        Logger('DataParse', mes, 'info')
        return params

    def _header(self):
        u"""创建session，修改header，参数为json格式"""
        session = requests.session()
        session.headers.update({'Content-Type': 'application/json'})
        return session

    def run(self):
        u"""运行用例，每个case进行签名并发送给接口，收到响应并返回"""
        results = list()
        for self.case in self.cases:
            params = self._datatypeparse()
            if self.ifsign == 1:
                params['sign'] = Encrypt().sign(params)

            params_json = json.dumps(params)
            response = self._header().post(self.url, params_json)
            result = dict()
            result['index'] = self.cases.index(self.case) + 1
            result['params'] = params_json
            result['response'] = response.content
            result['code'] = self.case['code']
            results.append(result)
            mes = "index: {0},response: {1},code: {2}"\
                .format(result['index'], result['response'], result['code'])
            Logger('CaseRun', mes, 'info')
        return results
