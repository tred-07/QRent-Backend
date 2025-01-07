from django.shortcuts import render
from rest_framework import viewsets, views, permissions, generics,serializers
from .models import RatingAndReviewModel
from.serializers import RatingAndReviewSerializer
# Create your views here.

class RatingView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset=RatingAndReviewModel.objects.all()
    serializer_class = RatingAndReviewSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)