# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     urls
   Description:
   Author:         thanksdanny(@hejunjie wechat:15521106117)
   date:          2019/10/17
-------------------------------------------------
   Change Activity:
                   2019/10/17
-------------------------------------------------
"""
__author__ = 'thanksdanny'

from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]
