from rest_framework import serializers

from .models import Proxie


class ProxieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proxie