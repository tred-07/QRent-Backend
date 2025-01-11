from django.urls import path,include

from rest_framework import routers
from .views import AdvertiseView,AdvertiseListView

router = routers.DefaultRouter()
router.register('create',AdvertiseView)

urlpatterns = [
    path('advertise/', include(router.urls)),
    path('',AdvertiseListView.as_view())
    # path('create/', AdvertiseView.as_view()),
]