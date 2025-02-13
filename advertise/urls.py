from django.urls import path,include

from rest_framework import routers
from .views import AdvertiseView,AdvertiseListView,AllAdvertise,UpdateAdvertise,AdDetailView,EditAd,AdDetailViewAll

router = routers.DefaultRouter()
router.register('create',AdvertiseView)

urlpatterns = [
    path('', include(router.urls)),
    path('all/',AllAdvertise.as_view(),name='all-add'),
    path('my/',AdvertiseListView.as_view(),name='my-add'),
    path('edit/<int:pk>/',EditAd.as_view()),
    path('<int:pk>/',AdDetailView.as_view()),
    path('all/<int:pk>/',AdDetailViewAll.as_view())
]