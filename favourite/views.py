from django.shortcuts import render
from rest_framework import viewsets, views, permissions, generics,serializers
from .models import FavouriteModel
from advertise.models import AdvertiseModel
from .serializers import FavouriteSerializer
# Create your views here.

class FavouriteView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = FavouriteModel.objects.all()
    serializer_class = FavouriteSerializer
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class CreateFavourite(generics.CreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=FavouriteSerializer
    # queryset=Review.objects.all()
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        return FavouriteModel.objects.filter(pk=pk)
    def perform_create(self,serializer):
        pk=self.kwargs.get('pk')
        watchlist=AdvertiseModel.objects.get(pk=pk)
        review_user=self.request.user
        review_queryset=FavouriteModel.objects.filter(advertise=watchlist,user=review_user)
        if review_queryset.exists():
            raise serializers.ValidationError("You have already added.")
        watchlist.save()
        serializer.save(advertise=watchlist,user=review_user)