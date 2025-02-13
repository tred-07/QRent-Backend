from django.urls import include, path
from rest_framework import routers
from .views import FavouriteView,CreateFavourite

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('list/',FavouriteView.as_view()),
    path('create/<int:pk>',CreateFavourite.as_view())
]