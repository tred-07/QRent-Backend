from .models import RequestModel
from rest_framework import serializers


class RequestSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    # advertise = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = RequestModel
        exclude=('advertise',)