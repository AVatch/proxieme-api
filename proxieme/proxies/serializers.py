from rest_framework import serializers

from .models import Proxie, Bid


class ProxieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proxie


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
