from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^add/', views.add_fine),
    url(r'^manage/$', views.manage_fines),
    url(r'^manage/(?P<id>[0-9]+)/', views.manage_user_fines),
    url(r'^manage/paid/', views.paid_status)
)
