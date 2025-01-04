from django.urls import include, path
from rest_framework import routers
from .views import FavouriteView

router = routers.DefaultRouter()
router.register('create', FavouriteView)

urlpatterns = [
    path('', include(router.urls)),
]