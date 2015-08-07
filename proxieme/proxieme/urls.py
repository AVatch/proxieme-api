from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import views

API_VERSION = 'v1'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/' + API_VERSION + '/$', views.api_root),

    url(r'^api/' + API_VERSION + '/', include('accounts.urls')),
)

urlpatterns += staticfiles_urlpatterns()