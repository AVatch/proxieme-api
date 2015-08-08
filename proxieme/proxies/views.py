from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Proxie
from .serializers import ProxieSerializer


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
