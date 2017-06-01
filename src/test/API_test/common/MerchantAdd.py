# coding:utf-8
import cx_Oracle
from tools.config import Config
from tools.encrypt import Encrypt
from tools.logger import log

from BaseModel import BaseModel
from src.utils.randomGen import random_string, random_number_str


class MerchantAdd(BaseModel):
    def __init__(self, userid=None):
        u"""如果没有传入userid，则新注册一个；同时初始化session，在header中规定格式为json；并默认一个随机的best_id号"""
        if userid is None:
            from User import User
            s = User()
            self.userid = s.signup()
        else:
            self.userid = userid
        self._changebestid()
        self.mobile = self._getusermobile()

    def _changebestid(self):
        u"""如果默认的best_id不能用，则随机换一个"""
        self.best_id = '10000' + random_number_str(4)

    def getmerchantid(self):
        u"""通过数据库获取商户merchant_id"""
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select merchantid from user_merchant t where t.userid='{0}'".format(self.userid))
        return cur.fetchone()[0]

    def _getbestid(self):
        u"""通过数据库获取绑定的best_id"""
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select bestid from u_bestbinding t where t.userid='{0}'".format(self.userid))
        try:
            return cur.fetchone()[0]
        except TypeError:
            print 'merchant did not bind a BEST id!'
            return None

    def return_best_id(self):
        return self._getbestid()

    def _getusermobile(self):
        u"""通过数据库获取商户mobile"""
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select mobile from user_info t where t.userid='{0}'".format(self.userid))
        return cur.fetchone()[0]

    def addstep1(self):
        u"""商户入驻第一步，信息都是随机字符串等，产生出通过第一步入驻的商户"""
        ran_str = random_string(15)
        param = {'p_userid': self.userid,
                  'p_enterpriseName': ran_str,
                  'p_enterpriseCode': ran_str,
                  'p_locationid': '110101',
                  'p_adress': ran_str,
                  'p_manageType': ran_str,
                  'p_referrer': 0,
                  'p_contacter': ran_str,
                  'p_contacterMobile': self.mobile,
                  'p_contacterEmail': ''
                 }
        return self._signandpost(param, 'AddStep1')

    def addstep2(self):
        u"""商户入驻第二步，上传图片，产生出通过第二步入驻的商户"""
        param = {'p_userid': self.userid,
                 'p_attachcount': 3,
                 'p_attachlist': '1[,]attach/ceshi/1.jpg[,]20180102[,][;]'
                                 '2[,]attach/ceshi/4.jpg[,]20180203[,][;]'
                                 '4[,]attach/ceshi/4.jpg[,]20180203[,][;]'
                 }
        return self._signandpost(param, 'AddStep2')

    def addstep3(self):
        u"""商户入驻第三步，提交后产生出提交审核的商户"""
        param = {'p_userid': self.userid,
                 'p_foundedtime': '20111111',
                 'p_registeredcapital': '',
                 'p_yearSalerroom': '',
                 'p_brand': '',
                 'p_ecinfo': '',
                 'p_offlineinfo': ''
                 }
        return self._signandpost(param, 'AddStep3')

    def bind(self):
        u"""商户审核通过后，绑定best，如果best绑定失败，换一个best账号，继续绑定，直到绑定成功，成功后可开通店铺"""
        param = {'user_id': self.userid,
                 'user_name': self.mobile,
                 'user_type': '2',
                 'id_code': self.best_id,
                 'BEST_user_id': self.best_id,
                 'BEST_password': Encrypt(pwd_key='111111').encrypt(self.best_id, 'MD5')}
        res = self._signandpost(param, 'Bind')
        log('Merchant - bind', res, 'info')
        # print res
        if res != '{}':
            self._changebestid()
            res = self.bind()
        # print res
        return res

    def unbind(self):
        u"""解绑best"""
        self.best_id = self._getbestid()
        param = {'user_id': self.userid,
                 'BEST_user_id': self.best_id,
                 'BEST_password': Encrypt(pwd_key='111111').encrypt(self.best_id, 'MD5')}
        return self._signandpost(param, 'UnBind')

    def openshop(self):
        u"""开通店铺，随机生成店铺名"""
        param = {'p_userid': self.userid,
                 'p_shopname': 'Py随机店铺' + random_string(10)}
        return self._signandpost(param, 'OpenShop')

    def getbasicstatus(self):
        u"""获取注册状态"""
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'GetBasicStatus')

    def getapplylist(self):
        u"""查看申请资料"""
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'GetApplyList')

    def approveapply(self, status=4):
        u"""审核商户，status=4为通过，status=5为驳回，默认值为4"""
        p_merchantid = self.getmerchantid()
        param = {'p_opid': 1,
                 'p_merchantid': p_merchantid,
                 'p_status': status,
                 'p_approvememo': random_string(15)}
        return self._signandpost(param, 'ApproveApply')

    def getbasicinfo(self):
        u"""管理员获取商户基本信息"""
        p_merchantid = self.getmerchantid()
        param = {'p_opid': 1,
                 'p_username': '',
                 'p_merchantid': p_merchantid,
                 'p_startdate': '10111111',
                 'p_enddate': '10111111',
                 'p_mobile': '',
                 'p_status': 4,
                 'p_approvename': ''}
        return self._signandpost(param, 'GetBasicinfo')

if __name__ == '__main__':
    merchant = MerchantAdd()
    # print merchant.getbasicinfo()
    # print merchant.addstep1()
    # print merchant.addstep2()
    # print merchant.addstep3()
    # print merchant.bind()
    # merchant.approveapply()
    # merchant.openshop()

    # print merchant.unbind()

