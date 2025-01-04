from django.shortcuts import render
from .serializers import AdvertiseSerializer
from .models import AdvertiseModel
from rest_framework import response,request,views,viewsets,permissions,generics,serializers
# Create your views here.

class AdvertiseView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = AdvertiseModel.objects.all()
    serializer_class = AdvertiseSerializer
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class AdvertiseListView(generics.ListAPIView):
    queryset = AdvertiseModel.objects.all()
    serializer_class = AdvertiseSerializer



    