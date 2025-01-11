from django.urls import path,include


from rest_framework import routers
from .views import UserViewSet, UserRegistration, UserLoginView, UserLogOutView

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('my/',UserViewSet.as_view()),
    path('register/', UserRegistration.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogOutView.as_view()),
]