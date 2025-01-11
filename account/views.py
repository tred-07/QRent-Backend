from django.shortcuts import render,redirect,HttpResponse
from rest_framework import viewsets,views
from .serializers import AccountModelSerializer,RegistrationSerializer,LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import tokens,authenticate,login,logout
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.views import generic
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
# permission_classes = [IsAuthenticated]
# Create your views here.

class UserViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = AccountModelSerializer

    def get_queryset(self):
        return super().get_queryset().filter(pk=self.request.user.pk)
    


class UserRegistration(APIView): # potato vs round-potato
    serializer_class=RegistrationSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token=tokens.default_token_generator.make_token(user)
            print("token ", token)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            print("uid",uid)
            # confirm_link=f"https://sdp-final-backend.vercel.app/user/active/{uid}/{token}" 
            # confirm_link=f"http://127.0.0.1:8000/user/active/{uid}/{token}"
            # email_subject="Confirm your account"
            # email_body=render_to_string('mail.html',{'confirm_link':confirm_link})
            # email=EmailMultiAlternatives(email_subject,"",to=[user.email])
            # email.attach_alternative(email_body,"text/html")
            # email.send()
            return Response("Done 1")
        return Response(serializer.errors)
    

class UserLoginView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user=authenticate(username=username,password=password)
            # print("Ok")
            if user:
                token,_=Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request,user)
                return Response({'token':token.key,'user_id':user.id})
                print("Ok")
            return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)


class UserLogOutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,req):
        # if req.is_authenticated():
        req.user.auth_token.delete()
        logout(req)
        return redirect('login')
    
'''   
class Activate(generic.View):
    def get(self,request,uid,token):
        try:
            uid=urlsafe_base64_decode(uid).decode()
            user=User. _default_manager.get(pk=uid)
        except(User.DoesNotExist):
            user=None

        if user is not None and tokens.default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            return redirect('https://qrent.vercel.app/login.html')

        return HttpResponse("You are not authenticated user.")
    



{
"username":"user2",
"password":"123456abcdef"
}
'''