# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/10
# python-version    : Python 3.7.0
# description       :

from django import forms
from db_model.models import User


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, kwargs)
        # self.initial['status'] = '00'

    # 00-有效  01-注销
    # status = forms.ChoiceField(label=u'账号状态', required=True, choices=(('00', '有效'), ("99", "注销")),
    #                            widget=forms.RadioSelect())

    class Meta:
        model = User
        exclude = ('userId',)
        fields = ['username', 'password', 'openId', 'is_active', 'is_staff',
                  'first_name', 'last_name', 'email', 'head', 'is_superuser', 'groups', 'user_permissions']
