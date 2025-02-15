from django.urls import path,include
from .views import RequestView, CreateRequest,EditRequest,ReqDetailView
from rest_framework import routers
router = routers.DefaultRouter()
urlpatterns = [
    # path('', include(router.urls)),
    path('create/<int:pk>/', CreateRequest.as_view(), name='create_review'),
    path('', RequestView.as_view(), name='request_list'),
    path('edit/<int:pk>/',EditRequest.as_view()),
    path('<int:pk>/',ReqDetailView.as_view())
]