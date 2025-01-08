from django.urls import path,include


from rest_framework import routers
from .views import UserViewSet, UserRegistration, UserLoginView, UserLogOutView

router = routers.DefaultRouter()
router.register('list', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistration.as_view()),
]