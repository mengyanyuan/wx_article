# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/6
# python-version    : Python 3.7.0
# description       :

from django.http import HttpResponse
from db_model.models import User


# def testdb(request):
#     user = User(userId='28045612534', openId='45tr498sd1ntyj_sdg', username='张三', head='/resources/images/6.jpg',
#                 status='00')
#     user.save()
#     return HttpResponse("<p>数据添加成功！</p>")

def testdb(request):
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = User.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = User.objects.filter(userId='28045612534')
    print(response2)

    # 获取单个对象
    user = User.objects.get(userId='28045612534')
    user.status = '01'
    user.save()
    print(user)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;可用于分页
    User.objects.order_by('-createTime')[0:2]

    # 数据排序
    User.objects.order_by('createTime')

    # 输出所有数据
    for item in list:
        response1 += item.userId + ","+item.username

    response = response1
    return HttpResponse("<p>"+response+"</p>")

