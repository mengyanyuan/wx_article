# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/8
# python-version    : Python 3.7.0
# description       : 文章操作服务类

import wx_articles.dao.article_dao as dao


def banner(*page):
    return dao.banner(page)


def get_articles(**params):
    return dao.get_articles(**params)
