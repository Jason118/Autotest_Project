# -*- coding: utf-8 -*-


class DataParser(object):
    """解析数据，主要用于将测试数据从数据文件中读取出来之后的处理（如按照类型转换，加密等），然后返回处理后的数据。"""

    def __init__(self, encrypt=None):
        """
        :t encrypt:加密信息，即Encrypt实例，包含私钥、盐以及默认加密方式
        """
        self.encrypt = encrypt

    def parse(self, data_list):
        """解析传入的data_list，[dict1,dict2,...]类型"""
        types = data_list[0]  # 第一项为类型
        datas = data_list[1:]  # 之后是待处理数据
        res = list()  # 最后返回的结果，也是个list，包括所有处理后的数据
        
        for item, p_type in types.items():
            if not p_type:
                types.pop(item)
        
        for data in datas:
            parsed = dict()
            for i, t in types.items():
                t = t.lower()
                try:
                    if t == 'int':
                        parsed[i] = int(data[i])
                    elif t == 'double':
                        parsed[i] = float(data[i])
                    elif t == 'str':
                        parsed[i] = data[i]
                    elif t == 'sha1':  # 传入具体的加密方式则表示不用盐加密，否则传入encrypt（用默认盐）
                        parsed[i] = self.encrypt.encrypt(data[i], salt='', encryway='SHA1')
                    elif t == 'md5':
                        parsed[i] = self.encrypt.encrypt(data[i], salt='', encryway='MD5')
                    elif t == 'encrypt':
                        parsed[i] = self.encrypt.encrypt(data[i])
                except (ValueError, AttributeError):
                    parsed[i] = data[i]
            res.append(parsed)

        return res


if __name__ == '__main__':
    d = [{'a': 'int', 'b': 'double', 'c': 'MD5'}, {'a': '1', 'b': '2', 'c': '1.0'}, {'a': 'a', 'b': 'b', 'c': 'c'}]
    from src.utils.encrypt import Encrypt
    print DataParser(Encrypt()).parse(d)

