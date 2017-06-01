# -*- coding: utf-8 -*-
from MerchantAdd import MerchantAdd


class Merchant(MerchantAdd):

    def add(self):
        u"""通过此方法直接生成商铺，减少中间重复的步骤，返回商铺merchant_id"""
        self.addstep1()
        self.addstep2()
        self.addstep3()
        self.approveapply()
        self.bind()
        self.openshop()
        return self.getmerchantid()

    def getuserid(self):
        u"""获取商户的userid"""
        return self.userid


if __name__ == '__main__':
    m = Merchant(userid=141)
    # print m.bind()
    # m.add()
    # print m.getuserid(), m.getmerchantid()