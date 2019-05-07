# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/1/29
# python-version    : Python 3.7.0
# description       : 字符串操作工具类

import random
import string


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
    def random_id(length, is_number=True):
        """
        生成指定长度的随机字符，默认只生成数字 \n
        :param length: 生成字符的长度
        :param is_number:  是否生成纯数字
        :return:
        """
        try:
            if length < 1:
                raise Exception(r'不能生成长度为%s的随机字符' % length)
            if is_number:
                "生成纯数字"
                return random.randrange(pow(10, length - 1), pow(10, length) - 1)
            else:
                "生成数字与字母混合随机字符串"
                return ''.join([random.choice(string.digits + string.ascii_letters) for i in range(length)])
        except Exception as e:
            print('生成随机字符失败，%s', e)
            return None
