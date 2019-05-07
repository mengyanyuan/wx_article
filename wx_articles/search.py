# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/6
# python-version    : Python 3.7.0
# description       :

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response, render


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为：' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


def search_post(request=HttpRequest()):
    ctx = {}
    print('远程IP:',request.META['REMOTE_ADDR'])
    print('全路径:',request.get_full_path())
    print('是否安全:',request.is_secure())
    if request.POST and 'content' in request.POST:
        ctx['rlt'] = request.POST['content']
    return render(request, "post.html", ctx)
