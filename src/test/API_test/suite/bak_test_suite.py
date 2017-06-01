# -*- coding: utf-8 -*-

import datetime
import unittest

from test.API_test.case import test_checkcode, test_checkname, test_getapplylist, test_getarea, test_getbasicstatus, \
    test_getmobile, test_getuserpasswordinfo
from test.API_test.case import test_collectionadd,test_collectiondelete,test_collectionget,test_personalapplypurchaser,\
    test_personalgethistorybill,test_personalgetmonthbill,test_personalgetpurchaser,test_personalinformation,\
    test_personalisrealname, test_personalupdatenikename,test_personalcentergetdetail,test_personalcentergetorder,\
    test_personalcenterlogistics,test_personalcenteruppasswd,test_realnamegetauthentication,test_realnameupauthentication,\
    test_userresetpassword,test_personalcentergetorderlist
from test.API_test.case import test_getbestid, test_buynow, test_getproductlist, test_navigation, \
    test_productgetcategory, test_productgetdetail, test_productgetdetailpic, \
    test_productgetlist, test_productgetrecmmendlist, test_productgetrecomm, test_productgetbrandlist, \
    test_orderget, test_presettlementcreate, test_presettlementget, test_shoppingcartdelete, \
    test_orderadd, test_productnavigation, test_productsearch, test_productsearchshop, \
    test_receiveaddradd, test_receiveaddrdefault, test_receiveaddrdelete, test_receiveaddrget,\
    test_shoppingcartupdate, test_shoppingcartnumber, test_shoppingcartget, test_shoppingcartadd, test_receiveaddrupdate,\
    test_purchasepay
from test.API_test.case import test_merchantcenterdelproduct

from src.utils import Config
from src.utils.reporter import HTMLTestRunner


def suite1():
    testsuite = unittest.TestSuite()

    testsuite.addTest(test_checkcode.TestCheckCode("test_checkcode"))
    testsuite.addTest(test_checkname.TestCheckName("test_checkname"))
    testsuite.addTest(test_getapplylist.TestGetApplyList("test_getapplylist"))
    testsuite.addTest(test_getarea.TestGetArea("test_getarea"))
    testsuite.addTest(test_getbasicstatus.TestGetBasicStatus("test_getbasicstatus"))
    testsuite.addTest(test_getmobile.TestGetMobile("test_getmobile"))
    testsuite.addTest(test_getuserpasswordinfo.TestGetUserPasswordInfo("test_getuserpasswordinfo"))
    return testsuite


def suite2():
    testsuite = unittest.TestSuite()

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_getbestid.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_buynow.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_getproductlist.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_navigation.cl))

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_productgetcategory.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_productgetdetail.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_productgetdetailpic.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_productgetlist.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_productgetrecmmendlist.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_productgetrecomm.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_productsearchshop.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_productsearch.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_productgetbrandlist.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_productnavigation.cl))

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_receiveaddradd.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_receiveaddrget.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_receiveaddrupdate.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_receiveaddrdefault.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_receiveaddrdelete.cl))

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_shoppingcartadd.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_shoppingcartget.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_shoppingcartnumber.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_shoppingcartdelete.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_shoppingcartupdate.cl))

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_orderadd.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_orderget.cl))

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_presettlementcreate.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_presettlementget.cl))

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_purchasepay.cl))

    return testsuite


def suite3():
    testsuite = unittest.TestSuite()

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_collectionadd.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_collectiondelete.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_collectionget.cl))

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_personalapplypurchaser.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_personalgethistorybill.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_personalgetmonthbill.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_personalgetpurchaser.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_personalinformation.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_personalisrealname.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_personalupdatenikename.cl))

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_personalcenterlogistics.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_personalcentergetorder.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_personalcenteruppasswd.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_personalcentergetdetail.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_personalcentergetorderlist.cl))

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_realnameupauthentication.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_realnamegetauthentication.cl))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_userresetpassword.cl))

    return testsuite


def suite4():
    testsuite = unittest.TestSuite()

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_merchantcenterdelproduct.cl))

    return testsuite


if __name__ == '__main__':
    """输出：TestReport_2016-01-01_153856.html"""
    filename = Config().get('report', 'path') + 'TestReport_{0}.html'\
        .format(datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S'))

    runner = HTMLTestRunner(stream=file(filename, 'wb'), title=u'直购接口测试报告', description='Test_Report')
    runner.run(suite3())
