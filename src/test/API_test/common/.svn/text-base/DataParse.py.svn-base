# -*- coding: utf-8 -*-
from src.utils import Encrypt
from src.utils import ReadXls
from src.utils import log


class DataParse:

    def __init__(self, datafile='zhigou.xlsx', sheet_name='sheet0', userid=None):
        self.datafile = datafile
        self.sheet_name = sheet_name
        self.userid = userid
        self.cases = ReadXls(self.datafile, sheet_name=self.sheet_name).get_data()
        self.types = self.cases.pop(0)

    # 在excel内需要特殊处理的值 与 指定的列类型
    CELLS = ['null', 'userid', '']
    TYPES = ['int', 'double', 'str', 'password', 'best', 'MD5']

    def do_int(self, par):
        try:
            res = int(par)
        except ValueError:
            res = par
        return res

    def do_double(self, par):
        try:
            res = float(par)
        except ValueError:
            res = par
        return res

    def do_str(self, par):
        return par

    def do_password(self, par):
        return Encrypt().encrypt(par, 'SHA1')

    def do_best(self, par, case):
        try:
            res = Encrypt(pwd_key=par).encrypt(case['BEST_user_id'], 'MD5')
            return res
        except KeyError:
            raise KeyError('Did not find key "BEST_user_id",check your data file!')

    def do_MD5(self, par):
        res = Encrypt(pwd_key='').encrypt(par, 'MD5')
        return res

    def do_cell(self, par):
        if par == 'null':
            res = None
        elif par == 'userid':
            res = self.userid
        return res

    TYPES_MAP = {'int': do_int, 'double': do_double, 'str': do_str, 'password': do_password, 'best': do_best}


    def dataparse(self):
        u"""将读取到的参数列表的第一项，即excel中的第二行，解析为参数的type，把所有的参数按照这个对应的type做处理。
        1.将所有为‘null’的字段都解析为None
        2.将type为‘int’的字段强制转换成int类型
        3.将type为‘str’的字段直接赋值
        4.将type为‘password’的字段进行加密，zhigou的加密方式为SHA1
        5.将type为‘best’的字段，加上盐，与id拼接并加密，zhigou的方式为MD5
        处理完之后，返回处理后的参数列表"""
        params_list = list()
        for case in self.cases:
            params = dict()
            mes = ''
            for key in self.types.keys():
                if case[key] in CELLS:
                    params[key] = self.do_cell(case[key])
                elif self.types[key] in TYPES:
                    if self.types[key] == 'int':
                        params[key] = self.do_int(case[key])
                    elif self.types[key] == 'str':
                        params[key] = self.do_str(case[key])
                    elif self.types[key] == 'password':
                        params[key] = self.do_password(case[key])
                    elif self.types[key] == 'best':
                        params[key] = self.do_best(case[key])
                    print key,params[key]
                    mes = mes + key + str(params[key]).decode('utf-8')
            log(mes, 'Case Data', 'info')
            params_list.append(params)
        return params_list

if __name__ == '__main__':
    dp = DataParse(datafile='shopping.xlsx', sheet_name='Navigation')
    print dp.dataparse()