from django.urls import path,include

from rest_framework import routers
from .views import AdvertiseView,AdvertiseListView,AllAdvertise

router = routers.DefaultRouter()
router.register('create',AdvertiseView)

urlpatterns = [
    path('advertise/', include(router.urls)),
    path('',AllAdvertise.as_view(),name='all-add'),
    path('my/',AdvertiseListView.as_view(),name='my-add')

    # path('create/', AdvertiseView.as_view()),
]