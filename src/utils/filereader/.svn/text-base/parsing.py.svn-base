# -*- coding: utf-8 -*-
"""一些解析工具方法"""
import string


def encode_unicode_bytes(my_string):
    """ 将 Unicode 字符串转为 UTF-8 字符串"""
    if not isinstance(my_string, basestring):
        my_string = repr(my_string)

    if isinstance(my_string, str):
        return my_string
    elif isinstance(my_string, unicode):
        return my_string.encode('utf-8')


def safe_substitute_unicode_template(templated_string, variable_map):
    """ 用 string.Template 的 safe_substitute 方法将传入的模板string 使用 variable_map进行解析，替换模板变量，返回str """

    my_template = string.Template(encode_unicode_bytes(templated_string))
    my_escaped_dict = dict(map(lambda x: (x[0], encode_unicode_bytes(x[1])), variable_map.items()))
    templated = my_template.safe_substitute(my_escaped_dict)
    return templated


def safe_to_json(in_obj):
    """ Safely get dict from object if present for json dumping """
    if isinstance(in_obj, bytearray):
        return str(in_obj)
    if hasattr(in_obj, '__dict__'):
        return in_obj.__dict__
    try:
        return str(in_obj)
    except:
        return repr(in_obj)


def flatten_dictionaries(input):
    """ 将一个列表中的字典合成一个字典，如果传入的不是一个列表，则直接返回 """
    output = dict()
    if isinstance(input, list):
        for map in input:
            output.update(map)
    else:  # Not a list of dictionaries
        output = input
    return output


def lowercase_keys(input_dict):
    """ 如果传入字典，则将字典中的所有key转为str并降为小写 """
    if not isinstance(input_dict, dict):
        return input_dict
    safe = dict()
    for key, value in input_dict.items():
        safe[str(key).lower()] = value
    return safe


def safe_to_bool(input):
    """ 将用户输出转化成boolean值，大小写不敏感。如果不是boolean或者不是符合 'true' 或 'false' 的str，则抛出异常 """
    if isinstance(input, bool):
        return input
    elif isinstance(input, basestring) and input.lower() == u'false':
        return False
    elif isinstance(input, basestring) and input.lower() == u'true':
        return True
    else:
        raise TypeError(
            'Input Object is not a boolean or string form of boolean!')
