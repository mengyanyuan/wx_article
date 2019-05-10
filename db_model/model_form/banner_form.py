# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/9
# python-version    : Python 3.7.0
# description       :

from db_model.models import Banner, Article
from django import forms


class BannerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BannerForm, self).__init__(*args, **kwargs)
        self.initial['type'] = '0'

    articleId = forms.ModelChoiceField(label=u'文章ID',required=False,queryset=Article.objects.order_by('date'))
    type = forms.ChoiceField(label=u'类型',
                             widget=forms.RadioSelect(),
                             choices=(('0', '图片'), ('1', '视频')))

    class Meta:
        model = Banner
        fields = ['title', 'articleId', 'resurl', 'type']
