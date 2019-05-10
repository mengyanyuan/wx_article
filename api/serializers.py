# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/8
# python-version    : Python 3.7.0
# description       : 序列化

from rest_framework import serializers
from db_model.models import *


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class RemarkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Remark
        fields = '__all__'


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        mmodel = Tag
        fields = '__all__'


class LikeRelSerializers(serializers.ModelSerializer):
    class Meta:
        model = LikeRel
        fields = '__all__'
