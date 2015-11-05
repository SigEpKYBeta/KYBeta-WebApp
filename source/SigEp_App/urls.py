from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SigEp_App.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index'),
    url(r'^index/', 'home.views.index'),
    url(r'^bms/', 'home.views.bms'),
    url(r'^contact/', 'home.views.contact'),
    url(r'^accounts/', include('accounts.urls'))
)
