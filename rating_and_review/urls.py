from django.urls import path,include
from rest_framework import routers
from .views import CreateRating,RatingAndReviewList
router = routers.DefaultRouter()

urlpatterns = [
    path('create/<int:pk>/',CreateRating.as_view(), name='create_rating'),
    path('<int:pk>/',RatingAndReviewList.as_view())
]