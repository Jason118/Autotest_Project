# -*- coding: utf-8 -*-
import json

from tools.config import Config

from BaseModel import BaseModel
from src.utils.randomGen import *


class OnlinePurchase(BaseModel):

    def __init__(self, userid):
        self.userid = userid
        self.prosettlementid = 0
        self.orderpageid = 0

    def ReceiveaddrAdd(self):
        param = {'p_userid': self.userid,
                 'p_receive_name': '{0}收货人{1}'.format(self.userid, random_string(4)),
                 'p_detail_address': '收货地址{0}'.format(random_string(4)),
                 'p_mobilephone': random_phone_number(),
                 'p_telephone': '11',
                 'p_locationid': '120101'
                 }
        return self._signandpost(param, 'ReceiveaddrAdd')

    def ReceiveaddrGet(self):
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'ReceiveaddrGet')

    def get_Receiveaddr_ids(self):
        res = self.ReceiveaddrGet()
        addrs = json.loads(res)['receiveaddress']
        addr_ids = list()
        for addr in addrs:
            addr_ids.append(addr['addressid'])
        return addr_ids

    def ShoppingCartAdd(self, merchant=30, product=1, countnum=5, spectypegroup_id='1*3'):
        param = {'p_userid': self.userid,
                 'p_merchantid': merchant,
                 'p_product_id': product,
                 'p_countnum': countnum,
                 'p_spectypegroup_id': spectypegroup_id
                 }
        return self._signandpost(param, 'ShoppingCartAdd')

    def ShoppingCartGet(self):
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'ShoppingCartGet')

    def get_Shopping_ids(self):
        res = self.ShoppingCartGet()
        shoppings = json.loads(res)['getshopcart']
        shopping_ids = list()
        for shopping in shoppings:
            shopping_ids.append(shopping['shoppingid'])
        return shopping_ids

    def get_Shopping_merchant_ids(self):
        res = self.ShoppingCartGet()
        shoppings = json.loads(res)['getshopcart']
        merchant_ids = list()
        for shopping in shoppings:
            merchant_ids.append(shopping['merchantid'])
        return merchant_ids

    def BuyNow(self, merchant=30, product=1, countnum=5, spectypegroup_id='1*3'):
        param = {'p_userid': self.userid,
                 'p_merchantid': merchant,
                 'p_product_id': product,
                 'p_countnum': countnum,
                 'p_spectypegroup_id': spectypegroup_id
                 }
        return self._signandpost(param, 'BuyNow')

    def list_to_str(self, list_bef, sep=','):
        string_aft = ''
        for index, item in enumerate(list_bef):
            # print index,
            # print len(list_bef)-1
            if index == len(list_bef)-1:
                string_aft += '{0}'.format(item)
            else:
                string_aft += '{0}{1}'.format(item, sep)
        return string_aft

    def PresettlementCreate(self):
        shoppingids = self.get_Shopping_ids()
        merchantids = self.get_Shopping_merchant_ids()
        param = {'p_userid': self.userid,
                 'p_shoppingid': self.list_to_str(shoppingids),
                 'p_merchantid': self.list_to_str(merchantids, sep=';')
                 }
        print param
        res = self._signandpost(param, 'PresettlementCreate')
        self.prosettlementid = json.loads(res)['p_prosettlementid']
        return res

    def PresettlementGet(self):
        param = {'p_userid': self.userid,
                 'p_prosettlementid': self.prosettlementid}
        return self._signandpost(param, 'PresettlementGet')

    def get_prosetpar_ids(self):
        res = self.PresettlementGet()
        presettlemnets = json.loads(res)['getpresettlement']
        prosetpar_ids = list()
        for presettlemnet in presettlemnets:
            prosetpar_ids.append(presettlemnet['prosetpar_id'])
        return prosetpar_ids

    def get_attachlist(self):
        res = self.PresettlementGet()
        presettlemnets = json.loads(res)['getpresettlement']
        p_attachlist = ''
        for presettlemnet in presettlemnets:
            p_attachlist += '{0}[,]1[,]发票信息详情{1}[,]备注{2}[,][;]'.format(presettlemnet['prosetpar_id'], random_string(5), random_string(5))
        return p_attachlist

    def OrderAdd(self):
        p_prosettlementids = self.get_prosetpar_ids()
        p_attachlist = ''
        for prosettlement in p_prosettlementids:
            p_attachlist += '{0}[,]1[,]发票信息详情{1}[,]备注{2}[,][;]'.format(prosettlement, random_string(5), random_string(5))
        param = {'p_userid': self.userid,
                 'p_prosettlementid': self.prosettlementid,
                 'p_prosetpar_id': self.list_to_str(p_prosettlementids, ';'),
                 'p_addressid': self.get_Receiveaddr_ids()[0],
                 'p_attachcount': len(p_prosettlementids),
                 'p_attachlist': p_attachlist
                 }
        print json.dumps(param, sort_keys=True, ensure_ascii=False, indent=4)
        res = self._signandpost(param, 'OrderAdd')
        self.orderpageid = json.loads(res)['orderid'][0]['orderpage_id']
        return res

    def OrderGet(self):
        param = {'p_userid': self.userid,
                 'p_orderpage_id': self.orderpageid
                 }
        # param = {'p_userid': 1082,
        #          'p_orderpage_id': 287
        #          }
        return self._signandpost(param, 'OrderGet')

    def get_order_ids(self):
        res = self.OrderGet()
        orders = json.loads(res)['orderdetail']
        order_ids = list()
        for order in orders:
            order_ids.append(order['order_id'])
        return order_ids

    def get_order_ids_from_db(self):
        import cx_Oracle
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select order_id from m_order t where t.userid='{0}'".format(self.userid))
        order_ids = []
        for i in cur.fetchall():
            order_ids.append(i[0])
        return order_ids

    def get_not_pay_order_from_db(self):
        import cx_Oracle
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select order_id from m_order t where t.userid='{0}' and t.status='0'".format(self.userid))
        return cur.fetchone()[0]

    def get_not_prepare_order_from_db(self):
        import cx_Oracle
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select order_id from m_order t where t.userid='{0}' and t.status='2'".format(self.userid))
        return cur.fetchone()[0]

    def get_not_send_order_from_db(self):
        import cx_Oracle
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select order_id from m_order t where t.userid='{0}' and t.status='3'".format(self.userid))
        return cur.fetchone()[0]

    def get_not_receive_order_from_db(self):
        import cx_Oracle
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select order_id from m_order t where t.userid='{0}' and t.status='4'".format(self.userid))
        return cur.fetchone()[0]

    def get_order_id_from_db(self):
        return self.get_order_ids_from_db()[0]

    def Purchase_Pay(self):
        from test.API_test.common.MerchantAdd import MerchantAdd
        from src.utils import Encrypt
        best_pass = Encrypt(pwd_key='').encrypt('{0}111111'.format(MerchantAdd(self.userid).return_best_id()), 'MD5')
        param = {'user_id': self.userid,
                 'best_pwd': best_pass,
                 'order_id': self.get_not_pay_order_from_db()
                 }
        return self._signandpost(param, 'PurchasePay')

    def Product_Search(self, content, asckey, asc, isquantity, page, n):
        param = {'p_searchcontent': content,
                 'p_asckey': asckey,
                 'p_asc': asc,
                 'p_isquantity': isquantity,
                 'p_page': page,
                 'p_n': n
                 }
        print param
        return self._signandpost(param, 'ProductSearch')


if __name__ == '__main__':
    # from User import User
    # u = User().signup()
    o = OnlinePurchase(45)
    # print o.BuyNow(merchant=30, product=1, countnum=1, spectypegroup_id='1*3')
    # print o.ReceiveaddrAdd()
    # print o.ReceiveaddrGet()
    # print o.ShoppingCartAdd(merchant=1708, product=164, countnum=1, spectypegroup_id='112*114')
    # print o.ShoppingCartGet()
    # # print o.get_Receiveaddr_ids()
    # print o.get_Shopping_ids()
    # print o.get_Shopping_merchant_ids()
    # print o.PresettlementCreate()
    # import json
    # print json.dumps(json.loads(o.PresettlementGet()), sort_keys=True, ensure_ascii=False, indent=4)
    # print o.OrderAdd()
    # print o.OrderGet()
    # print o.get_order_ids()
    # o = OnlinePurchase(141)
    # print o.get_order_ids_from_db()
    # print o.get_not_pay_order_from_db()
    # print o.Purchase_Pay()
    print o.Product_Search(content='', asckey='', asc='', isquantity=1, page=1, n=10)


