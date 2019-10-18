# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     urls.py
   Description:
   Author:         thanksdanny(@hejunjie wechat:15521106117)
   date:          2019/10/15
-------------------------------------------------
   Change Activity:
                   2019/10/15
-------------------------------------------------
"""
__author__ = 'thanksdanny'

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag')
]
