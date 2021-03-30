# -*- coding: utf-8 -*-

from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('add_izd/', views.add_izd, name='add_izd'),

]




