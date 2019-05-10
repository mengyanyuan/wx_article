# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/8
# python-version    : Python 3.7.0
# description       :

from django import forms

from db_model.models import *


class ArticleForm(forms.ModelForm):
    # 设置默认值
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.initial['status'] = '01'

    articleType = forms.ModelChoiceField(label=u'文章类型',
                                         queryset=Type.objects.filter(status='00'),
                                         widget=forms.Select())
    articleTags = forms.ModelMultipleChoiceField(label=u'标签',
                                                 queryset=Tag.objects.filter(status='00'),
                                                 widget=forms.CheckboxSelectMultiple())
    # 00-已发布  01-编辑中  02-审核中  99-已删除
    status = forms.ChoiceField(label=u'状态',choices=(("00", "已发布"), ("01", "编辑中"), ("02", "审核中"), ("99", "已删除")),
                               widget=forms.RadioSelect())

    class Meta:
        model = Article
        fields = ['articleTags']
