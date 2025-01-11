from django.db import models
from django.contrib.auth.models import User
from advertise.models import AdvertiseModel
# Create your models here.

class FavouriteModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="favourite")
    advertise = models.ForeignKey(AdvertiseModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
