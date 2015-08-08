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

    url(r'^proxies/(?P<pk>[0-9]+)/bids/$',
        views.ProxieBidList.as_view(),
        name='proxie-bid-list'),

    url(r'^proxies/(?P<pk>[0-9]+)/sessions/$',
        views.ProxieSessions.as_view(),
        name='proxie-sessions-list'),

    url(r'^bids/$',
        views.BidList.as_view(),
        name='bid-list'),

    url(r'^bids/(?P<pk>[0-9]+)/$',
        views.BidDetail.as_view(),
        name='bid-detail'),

    url(r'^proxiessessions/$',
        views.ProxieSessionList.as_view(),
        name='proxiessessions-list'),

    url(r'^proxiessessions/(?P<pk>[0-9]+)/$',
        views.ProxieSessionDetail.as_view(),
        name='proxiessessions-detail'),

])