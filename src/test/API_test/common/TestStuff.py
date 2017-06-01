# -*- coding: utf-8 -*-
import json
import unittest

from test.API_test.common.BaseCaseOperate import BaseCaseOperate
from test.API_test.common.Merchant import Merchant

from src.utils import Config
from src.utils import ReadXML

url_xml = Config().get('data', 'url_xml')


def generator(datafile='shopping.xlsx', sheet_name='sheet0', userid=None, prepare=False):
    u"""生成测试用例方法，传入data文件与sheet名，得到class"""

    class TestStuff(unittest.TestCase):
        #  基本类，同一类型的接口都可以用这个类来组织测试用例
        def setUp(self):
            u"""在setup中新生成一个user与merchant"""
            self.url = ReadXML(url_xml).get_url(sheet_name)
            print u'接口地址：{0}'.format(self.url)
            if userid is None:
                self.merchant = Merchant()
                self.merchant.add()
                self.userid = self.merchant.getuserid()
            else:
                self.userid = userid

        def test_stuff(self):
            #  读取相应数据文件，并执行用例，得到结果与datafile里的code列进行比较，从而验证是否成功
            results = BaseCaseOperate(self.url, datafile=datafile, sheet_name=sheet_name, userid=self.userid, prepare=prepare).run()
            for case in results:
                print u'用例编号：{0}'.format(case['index'])
                print u'传入参数：' # .format(case['params'])
                try:
                    print json.dumps(json.loads(case['params']), sort_keys=True, ensure_ascii=False, indent=4)
                except:
                    print unicode(case['params'])
                print u'返回值：'
                try:
                    print json.dumps(json.loads(case['response']), sort_keys=True, ensure_ascii=False, indent=4)
                except:
                    print unicode(case['response'])
                print u'期望代码：{0}'.format(case['code'])
                print
                self.assertIn(case['code'], case['response'])

    TestStuff.__name__ = 'Test' + sheet_name
    return TestStuff

if __name__ == '__main__':
    cl = generator(sheet_name='GetBestId')
    cl2 = generator(sheet_name='Navigation')
    suite = unittest.TestLoader().loadTestsFromTestCase(cl)
    suite.addTest(cl2('test_stuff'))
    unittest.TextTestRunner(verbosity=2).run(suite)