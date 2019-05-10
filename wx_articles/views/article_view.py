# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/8
# python-version    : Python 3.7.0
# description       :

from rest_framework import viewsets
from api.serializers import ArticleSerializers
import wx_articles.service.article_service as service
from api.paginator.paginator import PageSet


class ArticleViewSet(viewsets.ModelViewSet):
    """
    需要重写 get_queryset() 和 get_serializer_class() 方法，或者设置父类的 queryset 和 serializer_class
    """

    # queryset = service.get_articles()
    serializer_class = ArticleSerializers
    pagination_class = PageSet
