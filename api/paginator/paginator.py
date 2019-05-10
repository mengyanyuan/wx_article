# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/8
# python-version    : Python 3.7.0
# description       : 分页类

from rest_framework.pagination import PageNumberPagination
from core_common.constants.constants import CommonConstants as Consts


class PageSet(PageNumberPagination):
    # 配置每一页数据条数
    page_size = Consts.DEFAULT_PAGE_SIZE
    # 请求设置页面大小的参数名称，默认是None，表示客户端可能无法控制请求的页面大小。
    page_size_query_param = "size"
    # 最大允许请求的页面大小， 此属性仅在page_size_query_param也被设置时有效。
    max_page_size = Consts.MAX_PAGE_SIZE

    # 查询参数的名称，默认是'page'
    page_query_param = "page"

    # template：分页控件使用的模板的名称，可以覆盖或设置为None，默认为"rest_framework/pagination/numbers.html"
