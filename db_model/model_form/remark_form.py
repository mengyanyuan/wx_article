# -*-* encoding:UTF-8 -*-
# author            : mengy
# date              : 2019/5/10
# python-version    : Python 3.7.0
# description       : 

from django import forms
from db_model.models import Remark


class RemarkForm(forms.ModelForm):
    # 00-有效  01-待审核  99-已删除
    status = forms.ChoiceField(choices=(('00', '有效'), ('01', '待审核'), ('99', '已删除')),
                               widget=forms.RadioSelect(),
                               label=u'状态')

    class Meta:
        model = Remark
        fields = ['articleId', 'userId', 'content', 'status']
