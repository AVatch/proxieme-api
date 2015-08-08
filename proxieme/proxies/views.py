from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Proxie, Bid, ProxieSession
from .serializers import ProxieSerializer, BidSerializer, BidListSerializer, ProxieSessionListSerializer, ProxieSessionSerializer


class ProxiesList(generics.ListCreateAPIView):
    queryset = Proxie.objects.all()
    serializer_class = ProxieSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class ProxiesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proxie.objects.all()
    serializer_class = ProxieSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )


class ProxieBidList(generics.ListAPIView):
    serializer_class = BidListSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        proxie = get_object_or_404(Proxie, pk=self.kwargs['pk'])
        return Bid.objects.filter(proxie=proxie)


class BidList(generics.ListCreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class BidDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )


class ProxieSessionList(generics.ListCreateAPIView):
    queryset = ProxieSession.objects.all()
    serializer_class = ProxieSessionListSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )


class ProxieSessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProxieSession.objects.all()
    serializer_class = ProxieSessionSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )
