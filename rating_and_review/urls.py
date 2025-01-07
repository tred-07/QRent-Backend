from django.urls import path,include
from rest_framework import routers
from .views import RatingView
router = routers.DefaultRouter()

router.register("create-review",RatingView)

urlpatterns = [
    path("", include(router.urls)),
]