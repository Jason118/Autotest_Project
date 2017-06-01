# -*- coding: utf-8 -*-
"""自定义日志类，读取配置，并以配置为准进行日志输出，分别到console和log file里。

class:

Logger -- 日志类

    methods:

        __init__(logger_name='root')
            读入配置文件，进行配置。logger_name默认为root。

        get_logger()
            读取配置，添加相应handler，返回logger。
"""
import logging
from logging.handlers import TimedRotatingFileHandler
from src.utils.config import DefaultConfig


class Logger(object):

    def __init__(self, logger_name='root'):

        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)

        cf = DefaultConfig()
        self.log_path = cf.log_path
        self.log_file_name = cf.get('logging', 'log_file_name')
        self.backup_count = cf.getint('logging', 'backup_count')

        self.console_output_level = cf.get('logging', 'console_output_level')
        self.file_output_level = cf.get('logging', 'file_output_level')

        self.console_output = cf.getint('logging', 'console_output')
        self.file_output = cf.getint('logging', 'file_output')

        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            # if True, 在console中输出日志
            if self.console_output == 1:
                console_handler = logging.StreamHandler()
                console_handler.setFormatter(self.formatter)
                console_handler.setLevel(self.console_output_level)
                self.logger.addHandler(console_handler)
            else:
                pass

            # if True, 在日志文件中输出日志
            if self.file_output == 1:
                # 每天重新创建一个日志文件，最多保留backup_count份
                # todo: 这里应该有个bug，日志是看handler的时间而分日志，而不是自然日
                file_handler = TimedRotatingFileHandler(self.log_path + self.log_file_name, 'midnight', 1, self.backup_count)
                file_handler.setFormatter(self.formatter)
                file_handler.setLevel(self.file_output_level)
                self.logger.addHandler(file_handler)
            else:
                pass
        return self.logger


if __name__ == '__main__':
    logger = Logger().get_logger()

    logger.warning('hello world')
    logger.info('hi')
