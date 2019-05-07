# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/1/30
# python-version    : Python 3.7.0
# description       : 字典操作工具

import json


class Dict(dict):
    """
    字典操作工具类
    """
    # __setattr__ = super.__setitem__
    # __getattr__ = super.__getitem__

    @staticmethod
    def dict2obj(dictObj):
        """
        将字典转化成对象\n
        :param dictObj:
        :return:
        """
        try:
            if not isinstance(dictObj, dict):
                return dictObj
            inst = Dict()
            for k, v in dictObj.items():
                inst[k] = Dict.dict2obj(v)
            return inst
        except Exception as e:
            print('将字典转换成对象失败，%s', e)
            return None

    @staticmethod
    def str2dict(json_str):
        """
        将字符串转换成字典\n
        :param json_str:
        :return:
        """
        try:
            json_str = str.replace(json_str, '\'', '"')
            json_str = str.replace(json_str, '\\\\', '')
            json_str = str.replace(json_str, '\\n', '')
            return json.loads(json_str, encoding='utf-8')
        except Exception as e:
            print('将字符串转换成字典对象失败，%', e)
            return None


if __name__ == '__main__':
    # dicts = {'typeId': 3, 'typeName': '小说', 'status': '0', 'createTime': '2019-01-30 10:55:36'}
    #
    # inst = dict2obj(dicts)
    # print(inst.typeId)
    string = '{"typeId": 1,"typeName": "新闻","STATUS": "0","createTime": "2019-01-29 14:07:14"}'
    dict = Dict.str2dict(string)
    print(dict)
    print(type(dict))
