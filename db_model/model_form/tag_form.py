# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/8
# python-version    : Python 3.7.0
# description       :
from django import forms
from db_model.models import Tag


class TagForm(forms.ModelForm):
    # 设置默认值
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.initial['status'] = '00'

    tagName = forms.CharField(label=u'标签名', required=True, max_length=10,
                              error_messages={'required': u'标签名不能为空', 'max_length': '不能超过5个汉字'},
                              widget=forms.TextInput(attrs={'placeholder': u'标签名'}))
    status = forms.ChoiceField(label=u'状态',
                               widget=forms.RadioSelect(),
                               choices=(('00', '有效'), ('99', '失效')))

    class Meta:
        model = Tag
        fields = ['tagName', 'status']
