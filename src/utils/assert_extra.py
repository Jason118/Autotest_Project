#!/usr/bin/env python
#coding:utf-8

#Created on 2017年5月31日
__author__ = 'Jason'


def assertDictContainsSubset(expected, actual, msg=None):
    """Checks whether actual is a superset of expected."""
    missing = []
    mismatched = []
    for key, value in expected.iteritems():
        if key not in actual:
            missing.append(key)
        elif value != actual[key]:
            mismatched.append('%s, expected: %s, actual: %s' % (key, value,actual[key]))

    if not (missing or mismatched):
        return

    standardMsg = ''
    if missing:
        standardMsg = 'Missing: %s' % ','.join(m for m in missing)
    if mismatched:
        if standardMsg:
            standardMsg += '; '
        standardMsg += 'Mismatched values: %s' % ','.join(mismatched)

    if msg is None:
        raise Exception(standardMsg)
    else:
        try:
        # don't switch to '{}' formatting in Python 2.X
        # it changes the way unicode input is handled
            raise Exception('%s : %s' % (standardMsg, msg))
        except UnicodeDecodeError:
            raise  Exception('%s : %s' % (standardMsg, msg))