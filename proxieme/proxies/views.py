from django.shortcuts import get_object_or_404

from opentok import OpenTok
from opentok import Roles
from opentok import MediaModes

API_KEY = "45306032"
API_SECRET = "9399ba2cd2fef46d3f8ca1465519a9a5efe5505a"
OPENTOK_SDK = OpenTok(API_KEY, API_SECRET)

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

    def perform_create(self, serializer):
        session = OPENTOK_SDK.create_session(media_mode=MediaModes.routed)
        token1 = OPENTOK_SDK.generate_token(session.session_id, Roles.publisher)
        token2 = OPENTOK_SDK.generate_token(session.session_id, Roles.publisher)

        serializer.save(sessionID=session.session_id,
                        surrogateID=token1,
                        requesterID=token2)


class ProxieSessions(generics.ListAPIView):
    serializer_class = ProxieSessionSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        proxie = get_object_or_404(Proxie, pk=self.kwargs['pk'])
        return ProxieSession.objects.filter(proxie=proxie)


class ProxieSessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProxieSession.objects.all()
    serializer_class = ProxieSessionSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )
