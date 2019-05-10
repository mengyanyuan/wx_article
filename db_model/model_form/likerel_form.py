# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/10
# python-version    : Python 3.7.0
# description       :

from django import forms
from db_model.models import LikeRel


class LikeRelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LikeRelForm, self).__init__(*args, **kwargs)
        self.initial['type'] = '0'
        self.initial['status'] = '00'

    type = forms.ChoiceField(label=u'类型', choices=(('0', '点赞'), ('1', '收藏')), widget=forms.RadioSelect())
    status = forms.ChoiceField(label=u'状态', choices=(('00', '有效'), ('99', '取消')), widget=forms.RadioSelect())

    class Meta:
        model = LikeRel
        fields = ['articleId', 'userId', 'type', 'status']
