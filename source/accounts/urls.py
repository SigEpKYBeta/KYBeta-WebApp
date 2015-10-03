from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^/register/', views.register),
    url(r'^/register/success/', views.success, name='success'),
)
