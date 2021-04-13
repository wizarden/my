# -*- coding: utf-8 -*-

from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_izd/', views.list_izd, name='list_izd'),

]




