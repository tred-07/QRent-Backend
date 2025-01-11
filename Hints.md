<h3>Code from chatgpt</h3>

`models.py`
```py
from django.contrib.auth.models import AbstractUser
from django.db import models

# User model extension
class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=False)  # Account activation status

# Advertisement Model
class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Rent Request Model
class RentRequest(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    requester = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted')], default='Pending')

    def __str__(self):
        return f'Rent request for {self.advertisement.title}'

# Favorite Model
class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} favorited {self.advertisement.title}'

# Review and Rating Model
class Review(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comment = models.TextField()

    def __str__(self):
        return f'Review by {self.user.username} for {self.advertisement.title}'
```


`serializers.py`

```python
from rest_framework import serializers
from .models import CustomUser, Advertisement, RentRequest, Favorite, Review

# CustomUser Serializer (for registration)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

# Advertisement Serializer
class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'price', 'location', 'category', 'user', 'approved', 'created_at']

# Rent Request Serializer
class RentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentRequest
        fields = ['id', 'advertisement', 'requester', 'message', 'status']

# Favorite Serializer
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'advertisement']

# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'advertisement', 'user', 'rating', 'comment']
```

`views.py`

```python
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CustomUser, Advertisement, RentRequest, Favorite, Review
from .serializers import UserSerializer, AdvertisementSerializer, RentRequestSerializer, FavoriteSerializer, ReviewSerializer

# User Registration ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow public registration

# Advertisement ViewSet
class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        advertisement = self.get_object()
        advertisement.approved = True
        advertisement.save()
        return Response({'status': 'approved'})

# RentRequest ViewSet
class RentRequestViewSet(viewsets.ModelViewSet):
    queryset = RentRequest.objects.all()
    serializer_class = RentRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        rent_request = self.get_object()
        rent_request.status = 'Accepted'
        rent_request.save()

        # Mark other rent requests as rejected or close them
        RentRequest.objects.filter(advertisement=rent_request.advertisement, status='Pending').exclude(id=rent_request.id).update(status='Rejected')
        return Response({'status': 'accepted'})

# Favorite ViewSet
class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
```

`urls.py`

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'advertisements', views.AdvertisementViewSet)
router.register(r'rent-requests', views.RentRequestViewSet)
router.register(r'favorites', views.FavoriteViewSet)
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

`settings.py`

```py
INSTALLED_APPS = [
    # ... other installed apps
    'rest_framework',
    'rental',  # Your app name
]

# Configure the authentication settings (you can use Token or JWT authentication)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

