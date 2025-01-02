from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    is_rented = models.BooleanField(default=False)

    def __str__(self):
        return self.title
