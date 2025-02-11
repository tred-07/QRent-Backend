from django.shortcuts import render
from .serializers import AdvertiseSerializer
from .models import AdvertiseModel
from rest_framework import response,request,views,viewsets,permissions,generics,serializers,filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class AdvertiseView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = AdvertiseModel.objects.all()
    serializer_class = AdvertiseSerializer
    def perform_create(self,serializer):
        serializer.save(user=self.request.user,name=self.request.user.first_name)


class AdvertiseListView(generics.ListAPIView):
    queryset = AdvertiseModel.objects.all()
    serializer_class = AdvertiseSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['user__username','title','description','price',]
    ordering_fields=['price','created_at','updated_at']

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    

class AllAdvertise(generics.ListAPIView):
    queryset = AdvertiseModel.objects.all()
    serializer_class = AdvertiseSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['user__username','title','description','price',]
    ordering_fields=['price','created_at','updated_at']



class UpdateAdvertise(generics.UpdateAPIView):
    serializer_class=AdvertiseSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

class AdDetailView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    queryset = AdvertiseModel.objects.all()
    serializer_class = AdvertiseSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)





    