# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     forms
   Description:
   Author:         thanksdanny(@hejunjie wechat:15521106117)
   date:          2019/10/17
-------------------------------------------------
   Change Activity:
                   2019/10/17
-------------------------------------------------
"""
__author__ = 'thanksdanny'

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        """
        Meta里指定一些和表单相关的东西
        """
        model = Comment
        fields = ['name', 'email', 'url', 'text'] # 指明表单需要显示的字段
