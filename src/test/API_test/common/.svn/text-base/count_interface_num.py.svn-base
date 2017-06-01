# -*- coding: utf-8 -*-
"""这个文件用于统计api中的接口数量以及xml中的接口数量，以比对是否有漏掉或新加的接口"""
import requests
from bs4 import BeautifulSoup

from src.utils import Config

BASEURL = 'http://192.168.7.227:8080/zhigou/'
MERCHANT_SETTLED = 'doc.jsp?moduleName=merchant-settled'
ONLINE_PURCHASE = 'doc.jsp?moduleName=online-purchase'
PERSONAL_CENTER = 'doc.jsp?moduleName=personal-center'
MERCHANT_CENTER = 'doc.jsp?moduleName=merchant-center'


def get_api_num(url):
    req_url = BASEURL + url
    res = requests.get(req_url)
    res_soup = BeautifulSoup(res.content, 'html.parser')
    res_list = res_soup.find_all('a')
    for interface in res_list:
        if interface.string == u'【sample】':
            # print interface
            res_list.pop(res_list.index(interface))
        else:
            # print interface
            pass
    return len(res_list)


def get_all_api_num():
    api_sum = 0
    for url in [MERCHANT_SETTLED, ONLINE_PURCHASE, PERSONAL_CENTER, MERCHANT_CENTER]:
        print get_api_num(url)
        api_sum += get_api_num(url)
    return api_sum


def get_xml_api_num():
    api_sum = 0
    url_xml = Config().get('data', 'path') + Config().get('data', 'url_xml')
    res = BeautifulSoup(open(url_xml), 'xml')
    res_list = res.urls.contents
    for i in res_list:
        # print i.string[:1]
        if i != '\n' and i.string[:1] in ['P', 'R']:
            # print i.string
            api_sum += 1
    return api_sum


if __name__ == '__main__':
    print 'api中接口数量：{0}'.format(get_all_api_num())
    print 'xml中接口数量：{0}'.format(get_xml_api_num())
