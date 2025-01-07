from .models import RatingAndReviewModel
from rest_framework import serializers


class RatingAndReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = RatingAndReviewModel
        fields = '__all__'