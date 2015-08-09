from django.shortcuts import get_object_or_404, redirect

import braintree

from rest_framework import generics, status
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from proxies.models import Proxie, Bid, ProxieSession
from proxies.serializers import ProxieSerializer, BidListSerializer, ProxieSessionSerializer

from .models import Account
from .serializers import AccountSerializer

class AccountList(generics.ListAPIView):
    """
    URL: /api/v1/accounts/
    Methods: GET
    Returns: List of accounts
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class AccountCreate(generics.CreateAPIView):
    """
    URL: /api/v1/accounts/create/
    Methods: POST
    Returns: Creates an account
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = (CornellEmailCheck,)


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    URL: /api/v1/accounts/<pk>/
    Methods: GET, PUT, DELETE
    Returns: Handle an individual account object
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class AccountProxieList(generics.ListAPIView):
    serializer_class = ProxieSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        account = get_object_or_404(Account, pk=self.kwargs['pk'])
        return Proxie.objects.filter(account=account)


class AccountBidList(generics.ListAPIView):
    serializer_class = BidListSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        account = get_object_or_404(Account, pk=self.kwargs['pk'])
        return Bid.objects.filter(bidder=account)


class MeDetail(APIView):
    """
    URL: /api/v1/me/
    Methods: GET
    Returns: Account object of the authenticated user making the request.
    """
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        me = request.user
        serializer = AccountSerializer(me, context={'request': request})
        return Response(serializer.data)


class MeSurrogates(generics.ListAPIView):
    serializer_class = ProxieSessionSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        me = self.request.user
        return ProxieSession.objects.filter(surrogate_id=me)


class MeRequesters(generics.ListAPIView):
    serializer_class = ProxieSessionSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        me = self.request.user
        return ProxieSession.objects.filter(requester_id=me)


class Braintree(APIView):
    def get(self, request, format=None):
        try:
            braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="km4wdsbczwkb26vv",
                                  public_key="dkfsm9njgpkgw9k9",
                                  private_key="7ad555bb3d0feddba887d12d022b53ae")
            token = braintree.ClientToken.generate()
            response = {'token': token}
            return Response(response,
                        status=status.HTTP_200_OK)
        except Exception as e:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        print request.data
        origin = request.data.get('origin')
        try:
            braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="km4wdsbczwkb26vv",
                                  public_key="dkfsm9njgpkgw9k9",
                                  private_key="7ad555bb3d0feddba887d12d022b53ae")
            nonce = request.data.get('payment_method_nonce')
            amount = request.data.get('amount')
            
            result = braintree.Transaction.sale({
                "amount": amount,
                "payment_method_nonce": nonce
            })
            response = {"result": result}
            return redirect(origin)
        except Exception as e:
            print e
            return redirect(origin)

