# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/9
# python-version    : Python 3.7.0
# description       :

from db_model.models import Type
from django import forms


class TypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TypeForm, self).__init__(*args, **kwargs)
        self.initial['status'] = '00'

    typeName = forms.CharField(label=u'类型名', required=True, max_length=10,
                               error_messages={'required': u'类型名不能为空', 'max_length': '不能超过5个汉字'},
                               widget=forms.TextInput(attrs={'placeholder': u'类型名'}))
    status = forms.ChoiceField(label=u'状态',
                               widget=forms.RadioSelect(),
                               choices=(('00', '有效'), ('99', '失效')))

    class Meta:
        model = Type
        fields = ['typeName', 'status']
