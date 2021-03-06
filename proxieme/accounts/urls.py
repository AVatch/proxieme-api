from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views

import views

# API endpoints
urlpatterns = format_suffix_patterns([

    url(r'^accounts/$',
        views.AccountList.as_view(),
        name='account-list'),

    url(r'^accounts/create/$',
        views.AccountCreate.as_view(),
        name='account-create'),

    url(r'^accounts/(?P<pk>[0-9]+)/$',
        views.AccountDetail.as_view(),
        name='account-detail'),

    url(r'^accounts/(?P<pk>[0-9]+)/proxies/$',
        views.AccountProxieList.as_view(),
        name='account-proxie-list'),

    url(r'^accounts/(?P<pk>[0-9]+)/bids/$',
        views.AccountBidList.as_view(),
        name='account-bid-list'),

    url(r'^me/$',
        views.MeDetail.as_view(),
        name='me-detail'),

    url(r'^me/surrogates/$',
        views.MeSurrogates.as_view(),
        name='me-surrogate-list'),

    url(r'^me/requesters/$',
        views.MeRequesters.as_view(),
        name='me-requesters-list'),

    url(r'^braintree/$',
        views.Braintree.as_view(),
        name='braintree-token'),


])

# Get the auth token for the user
urlpatterns += [
    url(r'^api-token-auth/', rest_views.obtain_auth_token)
]
# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                                      namespace='rest_framework')),
]