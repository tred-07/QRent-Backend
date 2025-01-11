from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AdvertiseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="advertise")
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='advertise_image/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title} {self.user}"