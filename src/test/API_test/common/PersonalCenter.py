# -*- coding: utf-8 -*-
import cx_Oracle
from test.API_test.common.User import User
from tools.config import Config
from tools.encrypt import Encrypt

from src.utils.randomGen import random_string


class PersonalCenter(User):
    def __init__(self, mobile=None, username=None, password=None, userid=None):
        if userid is None:
            User.__init__(self, mobile=mobile, username=username, password=password)
            self.userid = self.signup()
        else:
            self.userid = userid

    def getmobile(self):
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select mobile from user_info t where t.userid='{0}'".format(self.userid))
        return cur.fetchone()[0]

    def collection_add(self, merchantid='', product_id=''):
        param = {'p_userid': self.userid, 'p_merchantid': merchantid, 'p_product_id': product_id}
        return self._signandpost(param, 'CollectionAdd')

    def collection_delete(self, merchantid='', product_id=''):
        param = {'p_userid': self.userid, 'p_merchantid': merchantid, 'p_product_id': product_id}
        return self._signandpost(param, 'CollectionDelete')

    def collection_get(self, collectiontype=0):
        param = {'p_userid': self.userid, 'p_collection_type': collectiontype}
        return self._signandpost(param, 'CollectionGet')

    def personal_againshopping(self, merchantid='', productid='', countnum='', spectypegroupid=''):
        param = {'p_userid': self.userid,
                 'p_merchantid': merchantid,
                 'p_product_id': productid,
                 'p_countnum': countnum,
                 'p_spectypegroup_id': spectypegroupid}
        return self._signandpost(param, 'PersonalAgainshopping')

    def personal_applypurchaser(self):
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'PersonalApplypurchaser')

    def personal_gethistorybill(self, begindate='2016-01-01', enddate='016-12-31'):
        param = {'p_userid': self.userid, 'p_begin_date': begindate, 'p_end_date': enddate}
        return self._signandpost(param, 'PersonalGethistorybill')

    def personal_getmonthbill(self):
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'PersonalGetmonthbill')

    def personal_getpurchaser(self):
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'PersonalGetpurchaser')

    def personal_information(self):
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'PersonalInformation')

    def personal_isrealname(self):
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'PersonalIsrealname')

    def personal_updatenikename(self, nickname=('user'+random_string(5))):
        param = {'p_userid': self.userid, 'p_nickname': nickname}
        return self._signandpost(param, 'PersonalUpdatenikename')

    def personalcenter_applyrefund(self, orderid):
        param = {'p_userid': self.userid, 'p_order_id': orderid}
        return self._signandpost(param, 'PersonalcenterApplyrefund')

    def personalcenter_getdetail(self, orderid):
        param = {'p_userid': self.userid, 'p_order_id': orderid}
        return self._signandpost(param, 'PersonalcenterGetdetail')

    def personalcenter_getorder(self, orderid):
        param = {'p_userid': self.userid, 'p_roder_id': orderid}
        return self._signandpost(param, 'PersonalcenterGetorder')

    def personalcenter_getorderlist(self, search='', status=0, startdate='20160101', enddate='20161231', page=1, n=10):
        param = {'p_userid': self.userid,
                 'p_search': search,
                 'p_status': status,
                 'p_startdate': startdate,
                 'p_enddate': enddate,
                 'p_page': page,
                 'p_n': n,
                 }
        print json.dumps(param, sort_keys=True, indent=4, ensure_ascii=True)
        return self._signandpost(param, 'PersonalcenterGetorderlist')

    def personalcenter_logistics(self, orderid):
        param = {'p_userid': self.userid, 'p_roder_id': orderid}
        return self._signandpost(param, 'PersonalcenterLogistics')

    def personalcenter_receive(self, orderid):
        param = {'p_userid': self.userid, 'p_roder_id': orderid}
        return self._signandpost(param, 'PersonalcenterReceive')

    def personalcenter_refunddetail(self, refundid):
        param = {'p_userid': self.userid, 'p_refund_id': refundid}
        return self._signandpost(param, 'PersonalcenterRefunddetail')

    def personalcenter_refundmanage(self):
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'PersonalcenterRefundmanage')

    def personalcenter_uppassword(self, oldpassword, newpassword):
        param = {'p_userid': self.userid, 'p_old_password': oldpassword, 'p_new_password': newpassword}
        return self._signandpost(param, 'PersonalcenterUppasswd')

    def personalcommit_applyrefund(self, orderid, refundfee, refundcasue):
        param = {'p_userid': self.userid, 'p_roder_id': orderid, 'p_refund_fee': refundfee, 'p_refund_casue': refundcasue}
        return self._signandpost(param, 'PersonalcommitApplyrefund')

    def realname_getauthentication(self):
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'RealnameGetauthentication')

    def realname_upauthentication(self, realname, idcardnumber, idcardfronturl, idcardbackurl):
        param = {'p_userid': self.userid,
                 'p_realname': realname,
                 'p_idcardnumber': idcardnumber,
                 'p_idcardfronturl': idcardfronturl,
                 'p_idcardbackurl': idcardbackurl
                 }
        return self._signandpost(param, 'RealnameUpauthentication')

    def user_resetpassword(self, password):
        param = {'p_mobile': self.getmobile(), 'p_password': Encrypt().encrypt(password, 'SHA1')}
        return self._signandpost(param, 'UserResetPassword')


if __name__ == '__main__':
    pc = PersonalCenter(userid=2082)
    # print pc.getmobile()
    # print pc.personal_updatenikename()
    import json
    print json.dumps(json.loads(pc.personalcenter_getorderlist(status=1, startdate='20150721',enddate='20160721', search='', n=20)), ensure_ascii=True, indent=4, sort_keys=True)
