# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/1/31
# python-version    : Python 3.7.0
# description       : 日志工具

import logging
import os
import time
import inspect
from common.constants.constants import CommonConstants as Consts
from common.utils.config_parse import Configuration

config = Configuration.config()

dir = os.path.dirname(Consts.LOG_FILE_PATH)
local_time = time.strftime('%Y-%m-%d', time.localtime())
handlers = {logging.NOTSET: os.path.join(dir, Consts.LOG_FILE_NOTSET % local_time),
            logging.DEBUG: os.path.join(dir, Consts.LOG_FILE_DEBUG % local_time),
            logging.INFO: os.path.join(dir, Consts.LOG_FILE_INFO % local_time),
            logging.WARNING: os.path.join(dir, Consts.LOG_FILE_WARNING % local_time),
            logging.ERROR: os.path.join(dir, Consts.LOG_FILE_ERROR % local_time),
            logging.CRITICAL: os.path.join(dir, Consts.LOG_FILE_CRITICAL % local_time),
            }


class Logger(object):
    """
    日志输出工具
    """
    __loggers = {}
    __config = Configuration.config()

    def printf_now(self):
        """
        输出当前时间\n
        :return:
        """
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def __create_hander(self, level):
        """
        创建日志的处理者\n
        :param level:
        :return:
        """
        log = logging.getLogger(str(level))
        # 如果已经存在handler，则不再创建
        if not log.handlers:
            path = handlers[level]
            log.setLevel(level)
            log_dir = config.get_value(Consts.LOG_SECTION, Consts.LOG_FILE_PATH)
            # 如果配置的日志文件路径不存在，则创建文件夹
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)
            file = logging.FileHandler(str(log_dir) + path,
                                       mode='a+', encoding='UTF-8')
            file.setLevel(level)
            console = logging.StreamHandler()
            console.setLevel(level)
            log.addHandler(file)
            log.addHandler(console)
            self.__loggers.update({level: log})

    def __get_log_msg(self, level, msg):
        frame, filename, line_no, function_name, code, unknow_field = inspect.stack()[2]
        return "[%s] [%s] [%s - %s - %s] %s" % (self.printf_now(), level, filename, line_no, function_name, msg)

    def info(self, msg, args=None):
        self.__create_hander(logging.INFO)
        msg = self.__get_log_msg("info", msg)
        if args:
            self.__loggers[logging.INFO].info(msg, args)
        else:
            self.__loggers[logging.INFO].info(msg)

    def debug(self, msg, args=None):
        self.__create_hander(logging.DEBUG)
        msg = self.__get_log_msg("debug", msg)
        if args:
            self.__loggers[logging.DEBUG].debug(msg, args)
        else:
            self.__loggers[logging.DEBUG].debug(msg)

    def warning(self, msg, args=None):
        self.__create_hander(logging.WARNING)
        msg = self.__get_log_msg("warning", msg)
        if args:
            self.__loggers[logging.WARNING].warning(msg, args)
        else:
            self.__loggers[logging.WARNING].warning(msg)

    def error(self, msg, args=None):
        self.__create_hander(logging.ERROR)
        msg = self.__get_log_msg("error", msg)
        if args:
            self.__loggers[logging.ERROR].error(msg, args)
        else:
            self.__loggers[logging.ERROR].error(msg)

    def critical(self, msg, args=None):
        self.__create_hander(logging.CRITICAL)
        msg = self.__get_log_msg("critical", msg)
        if args:
            self.__loggers[logging.CRITICAL].critical(msg, args)
        else:
            self.__loggers[logging.CRITICAL].critical(msg, args)


if __name__ == '__main__':
    logger = Logger()
    try:
        raise Exception('异常')
    except Exception as e:
        logger.debug('aaaa%s', e.args)
