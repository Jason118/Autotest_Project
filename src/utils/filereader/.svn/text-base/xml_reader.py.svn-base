# -*- coding: utf-8 -*-
"""从xml中获取页面链接或接口地址

For example:

    Data file like this:

        zhigou1.xml:

            <?xml version="1.0"?>
            <urls>
                <Base>http://192.168.7.227:8080/zhigou/</Base>

                <CheckCode>
                    P_Merchant__CheckCode
                    <type>POST</type>
                </CheckCode>
            </urls>

    Code:

        xml = ReadXML('zhigou1.xml')
        print xml.get_url('CheckCode')
        print xml.get_type('CheckCode')

    Result:

        http://192.168.7.227:8080/zhigou/P_Merchant__CheckCode
        POST

class:

ReadXML -- read xml and return api, and api type.

    methods:

        __init__(xml)
            read xml.

        base_url
            return the url in <Base></Base>

        get_url(tag)
            return interface url,which contact base_url with api text.

        get_type(tag)
            return interface type

        get_text(tag)
            return tag text.

"""
from xml.etree.ElementTree import ElementTree
from src.utils.config import DefaultConfig
from src.utils.utils_exception import DataFileNotAvailableException, DataError
from src.utils.logger import Logger


class XMLReader(object):

    def __init__(self, xml):
        self.logger = Logger(self.__class__.__name__).get_logger()
        self.xml = '{0}\\{1}'.format(DefaultConfig().data_path, xml)

        self.tree = self._tree()
        self.logger.info('read file: {0}'.format(self.xml))

    def _tree(self):
        try:
            return ElementTree(file=self.xml)
        except IOError as e:
            raise DataFileNotAvailableException(e)

    def get_url(self, tag):
        """Get interface url.

        :param tag: xml tag name.
        :return: base_url + tag text.
        """
        return self.base_url + self.get_text(tag)

    def get_text(self, tag):
        """Get tag text.

        :param tag: xml tag name or xpath.
        :return: tag text.
        """
        tree = self.tree
        try:
            return tree.find(tag).text.strip()
        except AttributeError:
            raise DataError('\'{0}\' does not have \'{1}\' element.Check your file.'.format(self.xml, tag))

    def get_type(self, tag):
        """Get interface type.

        :param tag: xml tag name.
        :return: interface type.
        """
        return self.get_text('.//{0}/type'.format(tag))

    def get_method(self, tag):
        """Get interface type.

        :param tag: xml tag name.
        :return: interface method.
        """
        return self.get_text('.//{0}/method'.format(tag))

    # todo: 补齐注释
    def get_file(self, tag):
        return self.get_text('.//{0}/file'.format(tag))

    def get_sheet(self, tag):
        return self.get_text('.//{0}/sheet'.format(tag))

    @property
    def base_url(self):
        """Get <Base></Base> text if exists."""
        return self.get_text('Base')

    def get_tags(self):
        base = self.tree.find('Base')
        tags = list()
        for element in self.tree.getroot().getchildren():
            if element != base:
                tags.append(element.tag)
        return tags


if __name__ == '__main__':
    x1 = XMLReader('zhigou.xml')
    # print x1.get_url('CheckCode')
    # print x1.get_type('CheckCode')
    # print x1.get_text('CheckCode')
    # print x1.base_url
    # print x1.get_all_interfaces()
    print x1.get_type('CheckCode')
    print x1.get_tags()