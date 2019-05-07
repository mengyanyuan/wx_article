# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/5
# python-version    : Python 3.7.0
# description       :

from django.shortcuts import render


def helle(request):
    context = {}
    context['hello'] = "Hello Django!"
    return render(request,'hello.html',context)

