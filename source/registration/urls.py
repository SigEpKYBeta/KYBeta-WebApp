from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^$', views.register),
    url(r'^/success/', views.success, name='success'),
)
