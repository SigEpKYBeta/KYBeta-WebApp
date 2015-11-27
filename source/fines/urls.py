from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^add/', views.add_fine),
    url(r'^manage/$', views.manage_fines),
)
