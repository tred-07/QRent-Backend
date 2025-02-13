from rest_framework import serializers
from .models import FavouriteModel

class FavouriteSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    advertise=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = FavouriteModel
        fields = '__all__'