from django.urls import path,include

from rest_framework import routers
from .views import AdvertiseView

router = routers.DefaultRouter()
router.register('create',AdvertiseView)

urlpatterns = [
    path('', include(router.urls)),
    # path('create/', AdvertiseView.as_view()),
]