from django.shortcuts import render
from rest_framework import viewsets, views, permissions, generics,serializers
from .models import RatingAndReviewModel
from.serializers import RatingAndReviewSerializer
from advertise.models import AdvertiseModel
from .permissions import AdminOrReadOnly
# Create your views here.

class RatingAndReviewList(generics.ListAPIView):
    queryset = RatingAndReviewModel.objects.all()
    serializer_class = RatingAndReviewSerializer
    permission_classes = [AdminOrReadOnly]
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class CreateRating(generics.CreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=RatingAndReviewSerializer
    # queryset=Review.objects.all()
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        return RatingAndReviewModel.objects.filter(pk=pk)
    def perform_create(self,serializer):
        pk=self.kwargs.get('pk')
        watchlist=AdvertiseModel.objects.get(pk=pk)
        review_user=self.request.user
        review_queryset=RatingAndReviewModel.objects.filter(advertise=watchlist,user=review_user)
        if review_queryset.exists():
            raise serializers.ValidationError("You have already reviewed.")
        watchlist.save()
        serializer.save(advertise=watchlist,user=review_user)