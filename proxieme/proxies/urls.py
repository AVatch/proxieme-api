from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

import views

# API endpoints
urlpatterns = format_suffix_patterns([

    url(r'^proxies/$',
        views.ProxiesList.as_view(),
        name='proxies-list'),

    url(r'^proxies/(?P<pk>[0-9]+)/$',
        views.ProxiesDetail.as_view(),
        name='proxies-detail'),

])