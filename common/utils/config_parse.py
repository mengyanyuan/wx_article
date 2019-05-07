# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/1/28
# python-version    : Python 3.7.0
# description       : 配置解析工具

import os
import configparser


class Configuration(object):
    """
    配置文件解析
    """

    def __init__(self, path=os.path.abspath(os.path.dirname(os.getcwd()) + './config/config.ini'), charset='utf-8'):
        # print('配置文件路径：', path)
        self.__config_path = path
        self.__config = configparser.ConfigParser()
        self.__config.read(path, charset)

    def get_configs(self, section):
        """
        根据片区获取该片区所有配置\n
        :param section: 片区名
        :return:
        """
        dicts = []
        try:
            if self.__config.has_section(section):
                options = self.__config.options(section)
                for option in options:
                    dicts.append({option: self.__config.get(section, option)})
        except Exception as e:
            print(e)
        return dicts

    def get_value(self, section, name):
        """
        根据片区名和配置名获取配置值\n
        :param section: 片区名
        :param name: 配置的key
        :return:
        """
        return self.__config.get(section, name)

    @staticmethod
    def config():
        """
        初始化默认配置解析对象，默认获取全局配置\n
        :return:
        """
        return Configuration()

# if __name__ == '__main__':
#     config = Configuration()
#     dicts = config.get_configs("DATASOURCE")
#     print(dicts)
#     print(config.get_value("DATASOURCE", "DB_NAME"))
