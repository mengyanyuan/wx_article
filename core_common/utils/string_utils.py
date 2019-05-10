# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/1/29
# python-version    : Python 3.7.0
# description       : 字符串操作工具类

import time, datetime, string, random


class String(object):
    """
    字符串工具类
    """

    @staticmethod
    def is_empty(str):
        """
        判断一个字符是否为空 \n
        :param str:
        :return:
        """
        return str is None or len(str) == 0 or len(str.strip()) == 0

    @staticmethod
    def is_not_empty(str):
        """
        判断一个字符是否不为空 \n
        :param str:
        :return:
        """
        return not String.is_empty(str)

    @staticmethod
    def random_id(length, is_number=True, start=''):
        """
        生成指定长度的随机字符，默认只生成数字 \n
        :param length: 生成字符的长度
        :param is_number:  是否生成纯数字
        :param start: 指定起始字符
        :return:
        """
        try:
            if length < 1:
                raise Exception(r'不能生成长度为%s的随机字符' % length)
            if is_number:
                "生成纯数字"
                return start + str(random.randrange(pow(10, length - 1), pow(10, length) - 1))
            else:
                "生成数字与字母混合随机字符串"
                return start + ''.join([random.choice(string.digits + string.ascii_letters) for i in range(length)])
        except Exception as e:
            print('生成随机字符失败，%s', e)
            return None

    @staticmethod
    def get_timestamp(locallize=False):
        """
        生成20位当前时间戳，locallize 为 True 时，返回当前毫秒值； locallize 为 False 时，返回本地化的时间戳\n
        :param locallize:是否本地化\n
        :return:
        """
        now = lambda: str(round(time.time() * 1e10))
        if locallize:
            now = lambda: str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))
        return now()


if __name__ == '__main__':
    print(String.get_timestamp())
    print(String.get_timestamp(True))
    print(len(String.get_timestamp(True)))

    print(String.random_id(length=6))
