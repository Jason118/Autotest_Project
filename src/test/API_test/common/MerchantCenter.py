# -*- coding: utf-8 -*-
import json

import cx_Oracle
from test.API_test.common.Merchant import Merchant
from tools.config import Config

from src.utils.randomGen import *


class MerchantCenter(Merchant):

    def add_brand(self, brandname='品牌{0}'.format(random_number_str(5)), brandlogo='logo.jpg', brandad='ad.jpg', brandintr=''):
        param = {'p_userid': self.userid,
                 'p_brand_name': brandname,
                 'p_brand_logo': brandlogo,
                 'p_brand_ad': brandad,
                 'p_brand_introduce': brandintr
                 }
        return self._signandpost(param, 'MerchantcenterAddbrand')

    def get_brand_ids(self):
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select brand_id from m_product_brand t where t.userid='{0}'".format(self.userid))
        return cur.fetchall()

    def update_brand(self, brandid, brandname, brandlogo, brandad, brandintr):
        param = {'p_userid': self.userid,
                 'p_brand_id': brandid,
                 'p_brand_name': brandname,
                 'p_brand_logo': brandlogo,
                 'p_brand_ad': brandad,
                 'p_brand_introduce': brandintr
                 }
        return self._signandpost(param, 'MerchantcenterUpdatebrand')

    def get_brand(self, page=1, n=10):
        param = {'p_userid': self.userid,
                 'p_page': page,
                 'p_n': n
                 }
        return self._signandpost(param, 'MerchantcenterGetbrand')

    def get_solo_brand(self, brandid):
        param = {'p_userid': self.userid,
                 'p_brand_id': brandid
                 }
        return self._signandpost(param, 'MerchantcenterGetsolobrand')

    def delete_brand(self, brandid):
        param = {'p_userid': self.userid,
                 'p_brand_id': brandid
                 }
        return self._signandpost(param, 'MerchantcenterDeletebrand')

    def add_custlist(self, userlevel=1, levelname='vip1', leveladdree='110101', username=''):
        param = {'p_userid': self.userid,
                 'p_userlevel': userlevel,
                 'p_levelname': levelname,
                 'p_leveladdree': leveladdree,
                 'p_username': username
                 }
        return self._signandpost(param, 'MerchantcenterAddcustlist')

    def customer_list(self, level=0, page=1, n=10):
        param = {'p_userid': self.userid,
                 'p_level': level,
                 'p_page': page,
                 'p_n': n
                 }
        return self._signandpost(param, 'MerchantcenterCustomerlist')

    def get_customer(self, levelid=1):
        param = {'p_userid': self.userid,
                 'p_levelid': levelid
                 }
        return self._signandpost(param, 'MerchantcenterGetcustomer')

    def get_username_from_db(self, levelname):
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select levelid from user_level t where t.levelname='{0}'".format(levelname))
        return cur.fetchone()[0]

    def get_category_id(self, category_level=2, parent=''):
        param = {'p_userid': self.userid,
                 'p_category_level': category_level,
                 'p_parent_id': parent
                 }
        return self._signandpost(param, 'MerchantcenterAddproduct1')

    def add_product_2(self, prod_name='云南普洱{0}'.format(random_number_str(5)), prod_type=57, orgin=530802,
                      grade='grade3', season='12month', variety='普洱', brand_id='', prod_desc=''):
        if brand_id == '':
            self.add_brand()
            brand_id = self.get_brand_ids()[0][0]
        param = {'p_userid': self.userid,
                 'p_product_name': prod_name,
                 'p_product_type': prod_type,
                 'p_orgin': orgin,
                 'p_grade': grade,
                 'p_season': season,
                 'p_variety': variety,
                 'p_brand_id': brand_id,
                 'p_product_describe': prod_desc
                 }
        res = self._signandpost(param, 'MerchantcenterAddproduct2')
        return json.loads(res)['p_product_id']

    def get_product_id(self):
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select product_id from product t where t.merchantid=(select merchantid from user_merchant u where u.userid='{0}')".format(self.userid))
        return cur.fetchone()[0]

    def add_product_3(self, product_id, spec_class='重量'):
        if not product_id:
            self.add_product_2()
        param = {'p_userid': self.userid,
                 'p_product_id': product_id,
                 'p_spec_class': spec_class
                 }
        print param
        res = self._signandpost(param, 'MerchantcenterAddproduct3')
        print res
        return json.loads(res)['specclass'][0]['speclass_id']

    def add_product_4(self, product_id, speclass, spec_type):
        param = {'p_userid': self.userid,
                 'p_product_id': product_id,
                 'p_speclass_id': speclass,
                 'p_spec_type': spec_type
                 }
        return self._signandpost(param, 'MerchantcenterAddproduct4')

    def sendaddr_add(self, send_name, address, mobile, location_id):
        param = {'p_userid': self.userid,
                 'p_send_name': send_name,
                 'p_detail_address': address,
                 'p_mobilephone': mobile,
                 'p_locationid': location_id
                 }
        return self._signandpost(param, 'SendaddrAdd')

    def sendaddr_get(self):
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'SendaddrGet')

    def get_send_address_id(self):
        res = self.sendaddr_get()
        return json.loads(res)['sendaddress'][0]['addressid']

    def on_shelves(self, product):
        param = {'p_userid': self.userid,
                 'p_product_id': product
                 }
        return self._signandpost(param, 'MerchantcenterOnshelves')

    def get_order_detail(self, order_id):
        param = {'p_userid': self.userid,
                 'p_order_id': order_id
                 }
        return self._signandpost(param, 'MerchantcenterGetdetail')

    def get_send_page(self, order_id):
        param = {'p_userid': self.userid,
                 'p_order_id': order_id
                 }
        return self._signandpost(param, 'MerchantcenterGetsend')

    def prepare(self, order_id):
        param = {'p_userid': self.userid,
                 'p_order_id': order_id
                 }
        return self._signandpost(param, 'MerchantcenterPrepare')

    def get_not_pay_order_from_db(self):
        import cx_Oracle
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select order_id from m_order t where t.meruserid='{0}' and t.status='0'".format(self.userid))
        return cur.fetchone()[0]

    def get_not_prepare_order_from_db(self):
        import cx_Oracle
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select order_id from m_order t where t.meruserid='{0}' and t.status='2'".format(self.userid))
        return cur.fetchone()[0]

    def get_not_send_order_from_db(self):
        import cx_Oracle
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select order_id from m_order t where t.meruserid='{0}' and t.status='3'".format(self.userid))
        return cur.fetchone()[0]

    def get_not_receive_order_from_db(self):
        import cx_Oracle
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select order_id from m_order t where t.meruserid='{0}' and t.status='4'".format(self.userid))
        return cur.fetchone()[0]

    def uplnventory(self, spec_id, quantity, quantityalert):
        param = {'p_userid': self.userid,
                 'p_spec_id': spec_id,
                 'p_quantity': quantity,
                 'p_quantityalert': quantityalert
                 }
        return self._signandpost(param, 'MerchantcenterUplnventory')

    def send(self, orderid, send_id, logistics_id, send_address, send_remarks):
        param = {'p_userid': self.userid,
                 'p_order_id': orderid,
                 'p_send_id': send_id,
                 'p_logistics_id': logistics_id,
                 'p_send_addressid': send_address,
                 'p_send_remarks': send_remarks
                 }
        return self._signandpost(param, 'MerchantcenterSend')

    def upcustlist(self, levelid, levelname, leveladdress, userlevel):
        param = {'p_userid': self.userid,
                 'p_levelid': levelid,
                 'p_levelname': levelname,
                 'p_leveladdree': leveladdress,
                 'p_userlevel': userlevel}
        print json.dumps(param, ensure_ascii=True, indent=4, sort_keys=True)
        return self._signandpost(param, 'MerchantcenterUpcustlist')


if __name__ == '__main__':
    s = MerchantCenter(userid=1892)
    # print s.add_brand(brandname='xxx', brandad='s.jpg', brandlogo='j.jpg', brandintr='xxxxxx')
    # print s.get_brand_ids()
    # from tools.random_gen import random_phone_number
    # print s.add_custlist(username='15876862305')
    # print s.customer_list()
    # print s.get_username_from_db()
    # print s.get_category_id(4, 19)
    # print s.get_product_id()
    # print s.add_product_2(brand_id=s.get_brand_ids()[0][0], prod_desc='普洱')
    # print s.add_product_3(s.add_product_2(brand_id=s.get_brand_ids()[0][0]), spec_class='包装,重量')
    # print s.add_product_4(product_id=164, speclass=216, spec_type='小盒')
    # print s.add_product_4(product_id=164, speclass=216, spec_type='大盒')
    # print s.add_product_4(product_id=164, speclass=217, spec_type='20g')
    # print s.add_product_4(product_id=164, speclass=216, spec_type='30g')
    # print s.sendaddr_add(send_name='James', address='TianJin', mobile='12345678969', location_id='110101')
    # print s.get_send_address_id()
    # print s.on_shelves(164)
    # print s.get_order_detail(order_id='2016071911255416097')
    # print s.prepare(order_id='2016071911255416097')
    # print s.get_send_page(order_id='2016071911255416097')
    # print s.get_not_prepare_order_from_db()
    # print s.get_not_send_order_from_db()
    # print s.uplnventory(spec_id=662, quantity=10000, quantityalert=10)
    print s.upcustlist(levelid=189, userlevel=3, levelname='111', leveladdress=120105)