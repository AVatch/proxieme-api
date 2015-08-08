from rest_framework import serializers

from accounts.serializers import AccountSerializer

from .models import Proxie, Bid, ProxieSession


class ProxieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proxie


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid

class BidListSerializer(serializers.ModelSerializer):
    bidder = AccountSerializer()
    class Meta:
        model = Bid

class ProxieSessionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProxieSession

class ProxieSessionSerializer(serializers.ModelSerializer):
    bid = BidSerializer()
    proxie = ProxieSerializer()
    surrogate = AccountSerializer()
    requester = AccountSerializer()

    class Meta:
        model = ProxieSession