from django.shortcuts import render
from rest_framework import viewsets, views, permissions, generics,serializers
from .models import FavouriteModel
from .serializers import FavouriteSerializer
# Create your views here.

class FavouriteView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = FavouriteModel.objects.all()
    serializer_class = FavouriteSerializer
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
