from django.shortcuts import render
from .serializers import RequestSerializer
from .models import RequestModel
from rest_framework import generics,viewsets,serializers,permissions,views,response
from advertise.models import AdvertiseModel
# Create your views here.


class RequestView(generics.ListAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer


class CreateRequest(generics.CreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=RequestSerializer
    # queryset=Review.objects.all()
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        return RequestModel.objects.filter(pk=pk)
    def perform_create(self,serializer):
        pk=self.kwargs.get('pk')
        watchlist=AdvertiseModel.objects.get(pk=pk)
        review_user=self.request.user
        review_queryset=RequestModel.objects.filter(advertise=watchlist,user=review_user,name=review_user.first_name+" "+review_user.last_name)
        if review_queryset.exists():
            raise serializers.ValidationError("You have already requested.")
        watchlist.save()
        serializer.save(advertise=watchlist,user=review_user,name=review_user.first_name+" "+review_user.last_name)



class EditRequest(views.APIView):
    permission_classes=[permissions.IsAuthenticated]
    def put(self,request,pk): # u = update operation
        request1=RequestModel.objects.get(pk=pk)
        serializer=RequestSerializer(request1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        else:
            return response.Response(serializer.errors)