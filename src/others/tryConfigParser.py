# -*- coding: utf-8 -*-

from ConfigParser import ConfigParser

cf = ConfigParser()
cf.read('../../config/config.ini')
print cf.sections()
print cf.options('path')
print cf.has_section('db')
print cf.has_option('db', 'port')
print cf.has_option('db', 'xx')
print cf.get('path', 'log')
print cf.items('path')