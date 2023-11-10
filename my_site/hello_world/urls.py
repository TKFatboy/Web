##from django.conf.urls import url
##from django.urls import include, re_path
from . import views
##from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home2/', views.home2, name='home2'),
    path('read/', views.read1, name='read'),
    path('read2/', views.read2, name='read2'),
    path('read3/', views.read3, name='read3'),
    path('read4/', views.read4, name='read4'),
    path('read5/', views.read5, name='read5'),
    path('search/', views.search, name='search'),
    path('info/', views.info, name='info'),
    path('test/', views.test, name='test'),
    path('action/', views.action, name='action'),
    path('adventure/', views.adventure, name='adventure'),
    path('comedy/', views.comedy, name='comedy'),
    path('drama/', views.drama, name='drama'),
    path('fantasy/', views.fantasy, name='fantasy'),
    path('horror/', views.horror, name='horror'),
    path('romance/', views.romance, name='romance'),
    path('thriller/', views.thriller, name='thriller'),
    path('western/', views.western, name='western'),
    path('scifi/', views.scifi, name='scifi'),
    path('crime/', views.crime, name='crime'),
    path('mystery/', views.mystery, name='mystery'),

]