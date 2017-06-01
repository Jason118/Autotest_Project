# -*- coding: utf-8 -*-

from excel_reader import ExcelReader
from xml_reader import XMLReader
from yaml_reader import YamlReader


class FileReader(object):

    def __init__(self, file_info, reader=None):
        self.file_info = file_info
        if isinstance(self.file_info, dict):
            self.file = self.file_info['file']
        elif isinstance(self.file_info, basestring):
            self.file = self.file_info

        if reader:
            self.reader = reader
        else:
            self.reader = self._check_type()

    def _check_type(self):
        file_type = self.file.split('.').pop(-1)
        if file_type == 'xls' or file_type == 'xlsx':
            return 'ExcelReader'
        elif file_type == 'xml':
            return 'XMLReader'
        elif file_type == 'yaml' or file_type == 'yml':
            return 'YamlReader'

    def read(self):
        if self.reader == 'ExcelReader':
            sheet = self.file_info['sheet'] if 'sheet' in self.file_info else 0
            r = ExcelReader(self.file, sheet=sheet)
            if 'iteration' in self.file_info:
                re_list = list()
                re_list.append(r.data[0])
                if isinstance(self.file_info['iteration'], list):
                    re_list.append(r.data[self.file_info['iteration'][0]:self.file_info['iteration'][1]+1])
                elif isinstance(self.file_info['iteration'], tuple):
                    for item in self.file_info['iteration']:
                        re_list.append(r.data[item])
                return re_list
            else:
                return r.data
        elif self.reader == 'XMLReader':
            return XMLReader(self.file)
        elif self.reader == 'YamlReader':
            return YamlReader(self.file)


if __name__ == '__main__':
    f = {'file': 'zhigou.xlsx', 'sheet': 'CheckCode', 'iteration': [3, 10]}
    print FileReader(f).read()
    # f2 = {'file': 'zhigou.xml'}
    # print FileReader(f2).read().get_tags()
    # f3 = {'file': 'test.yaml'}
    # print FileReader(f3).read().yaml
