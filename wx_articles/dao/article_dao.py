# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/7
# python-version    : Python 3.7.0
# description       : 文章的数据操作类

from db_model.models import *
from wx_articles.common.consts import Consts


def banner(*page):
    page_no = int(page[0]) if not page and not page[0] else Consts.DEFAULT_PAGE_NO
    page_size = int(page[1]) if not page and not page[1] else Consts.DEFAULT_PAGE_SIZE

    print(page_no)
    print(page_size)
    print(Banner.objects.order_by('createTime')[page_no, page_size])


def get_articles(**params):
    # page_no = int(params['page']) if not params and not params['page'] else Consts.DEFAULT_PAGE_NO
    # page_size = int(params['size']) if not params and not params['size'] else Consts.DEFAULT_PAGE_SIZE

    page_no = 0
    page_size = 5
    articles = Article.objects.order_by('-createTime')
    print(articles)
    return articles
