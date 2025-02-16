from django.db import models
from django.contrib.auth.models import User
from advertise.models import AdvertiseModel
# Create your models here.

class RequestModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="request")
    advertise= models.ForeignKey(AdvertiseModel, on_delete=models.CASCADE,related_name="request")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    name=models.CharField(blank=True,max_length=20)
    def __str__(self):
        return f"{self.user} {self.advertise} {self.is_accepted}"