from django.db import models
from advertise.models import Ad
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.reviewer} for ad {self.ad}'
