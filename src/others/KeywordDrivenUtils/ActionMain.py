# -*- coding: utf-8 -*-
from ActionKeys import *


action_dict = {'openbrowser': open_browser, 'get': get, 'sendkeys': send_keys,
               'clear': clear, 'click': click, 'close': close, 'quit': quitdriver,
               'wait': wait
               }
arg_list = ['action', 'browser', 'url', 'by', 'value', 'text', 'time']


class UnknownArgs(StandardError):
    pass


class UnknownAction(StandardError):
    pass


def checkargs(keymap):
    for keys in keymap:
        result = list(set(keys.keys()) ^ set(arg_list))
        if not result:
            if keys['action'] in action_dict.keys():
                pass
            else:
                log('action check failed', u'unknown action {0}'.format(keys['action']))
                raise UnknownAction(msg=u'unknown action {0}'.format(keys['action']))
        else:
            log('args check failed', u'unknown args {0}'.format(str(result)))
            raise UnknownArgs(msg=u'unknown args {0}'.format(str(result)))


def run(keymap):
    checkargs(keymap)
    driver = None
    for keys in keymap:
        action = action_dict[keys['action']]
        browser = keys['browser']
        url = unicode(keys['url'], 'utf-8')
        by = keys['by']
        value = unicode(keys['value'], 'utf-8')
        text = unicode(keys['text'], 'utf-8')
        time = keys['time']
        print action, browser, url, by, value, text
        driver = action(driver=driver, browser=browser, url=url, by=by, value=value, text=text, t=time)


if __name__ == '__main__':
    from src.utils import ReadXls
    ks = ReadXls('keyworddriven.xlsx').get_data()
    run(ks)

