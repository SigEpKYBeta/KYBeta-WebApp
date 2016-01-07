from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^member/', include('member_home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index'),
    url(r'^index/', 'home.views.index'),
    url(r'^bms/', 'home.views.bms'),
    url(r'^contact/', 'home.views.contact'),
    url(r'^comingsoon/', 'home.views.coming_soon'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^fines/', include('fines.urls'))
)
