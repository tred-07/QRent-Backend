from rest_framework import serializers
from .models import AdvertiseModel

class AdvertiseSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = AdvertiseModel
        exclude = ('is_approved',)
        