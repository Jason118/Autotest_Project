#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/1 9:27
# @Author  : Terry
import re


def update(str_message, str_current_issue, str_splitor="X"):
    """
    将当前期数插入到期待消息中。
    当投注成功时，会弹出“您确定加入 620927 期？”消息。
    测试数据中，【期待消息】为“您确定加入 X 期？”，无法与实际消息匹配。
    所以，该方法使用实际的当前期数替换【期待消息】中的字符X。
    :param str_message: 测试数据中的【期待消息】，例如“您确定加入 X 期？”。
    :param str_current_issue: 实际的当前期数，例如620927。
    :param str_splitor: 待替换的字符。
    :return: 返回更新后的【期待消息】
    """
    if len(str_message):
        pattern = re.compile(str_splitor)
        match = pattern.search(str_message)
        if match:
            lis_messsage = str(str_message).split(str_splitor)
            for i in range(len(lis_messsage)):
                lis_messsage[i] = lis_messsage[i].strip(' \t\n\r')
            return (" %s " % str_current_issue).join(lis_messsage)
        else:
            raise Exception("\nInvalid splitor.\nCan not find splitor:%s in message:%s." % (str_splitor, str_message))

    else:
        raise Exception("\nPop up message can not be empty!")
