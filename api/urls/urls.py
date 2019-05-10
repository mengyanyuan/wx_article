# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/8
# python-version    : Python 3.7.0
# description       : api入口

from django.conf.urls import include, url
from rest_framework import routers
from wx_articles.views.article_view import ArticleViewSet

# 定义路由地址
route = routers.DefaultRouter()

# 注册新的路由地址
route.register(r'articles', ArticleViewSet, base_name='articles')

# 注册上一级的路由地址并添加
urlpatterns = [
    url('api/', include(route.urls)),
]
