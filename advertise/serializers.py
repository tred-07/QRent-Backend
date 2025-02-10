from rest_framework import serializers
from .models import AdvertiseModel
from request.serializers import RequestSerializer
from rating_and_review.serializers import RatingAndReviewSerializer
class AdvertiseSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    request=RequestSerializer(read_only=True,many=True)
    review=RatingAndReviewSerializer(read_only=True,many=True)
    class Meta:
        model = AdvertiseModel
        fields = '__all__'
        exclude='is_approved'
        