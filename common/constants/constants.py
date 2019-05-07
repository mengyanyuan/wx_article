# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/1/28
# python-version    : Python 3.7.0
# description       : 常量


class CommonConstants(object):
    """
    常量
    """
    # 数据库
    DB_SECTION = "DATASOURCE"
    DB_URL = "DB_URL"
    DB_PORT = "DB_PORT"
    DB_NAME = "DB_NAME"
    DB_USERNAME = "DB_USERNAME"
    DB_PASSWORD = "DB_PASSWORD"
    DB_CHARSET = "DB_CHARSET"
    DB_SHOW_SQL = "DB_SHOW_SQL"

    # 缓存
    CACHE_SECTION = "CACHE"
    CACHE_HOST = "CACHE_HOST"
    CACHE_PORT = "CACHE_PORT"
    CACHE_DECODE_RESPONSES = "CACHE_DECODE_RESPONSES"
    CACHE_TAG = "_wx_microapp_tag_"
    CACHE_TYPE = "_wx_microapp_type_"

    # SQL 类型
    SQL_TYPE_SELECT = 'select'
    SQL_TYPE_UPDATE = 'update'
    SQL_TYPE_DELETE = 'delete'
    SQL_TYPE_INSERT = 'insert'

    # 日志
    LOG_SECTION = "LOGGER"
    LOG_FORMAT = "LOG_FORMAT"
    LOG_LEVEL = "LOG_LEVEL"
    LOG_FILE_PATH = "LOG_FILE_PATH"
    # 默认日志存放文件
    LOG_FILE_NOTSET = "notset_%s.log"
    # DEBUG 日志文件
    LOG_FILE_DEBUG = "debug_%s.log"
    # INFO 日志文件
    LOG_FILE_INFO = "info_%s.log"
    # WARNING 日志文件
    LOG_FILE_WARNING = "warning_%s.log"
    # ERROR 日志文件
    LOG_FILE_ERROR = "error_%s.log"
    # CRITICAL 日志文件
    LOG_FILE_CRITICAL = "critical_%s.log"

    # 微信接口
    WX_IF_HOST = "HOST"
    WX_MICRO_APP = "MICRO-APP"
    WX_APPID = "APPID"
    WX_APPSECRET = "APPSECRET"
    WX_JSCODE = "JSCODE"
    WX_AUTHORIZATION_URL = "AUTHORIZATION_URL"

    # 分页
    DEFAULT_PAGE_NO = 0
    DEFAULT_PAGE_SIZE = 5

    # session


