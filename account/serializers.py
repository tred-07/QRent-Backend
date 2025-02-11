from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AccountModel
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from advertise.serializers import AdvertiseSerializer
from favourite.serializers import FavouriteSerializer
from rating_and_review.serializers import RatingAndReviewSerializer
from request.serializers import RequestSerializer


class AccountModelSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]
    user=serializers.StringRelatedField(many=False)
    advertise=AdvertiseSerializer(many=True)
    feedback=FavouriteSerializer(many= True)
    favourite=FavouriteSerializer(many=True)
    request=RequestSerializer(many=True)
    class Meta:
        model=User
        fields='__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm_password']

    def save(self):
        username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email=self.validated_data['email']
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']

        if password!=confirm_password:
            raise serializers.ValidationError({'error':'Password Does Not Match'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':'Email already exist'})
        account=User(username=username,first_name=first_name,last_name=last_name,email=email)
        account.is_active=False
        account.set_password(password)
        account.save()
        return account
    

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)