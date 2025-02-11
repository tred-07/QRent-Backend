from django.db import models
from django.contrib.auth.models import User
from advertise.models import AdvertiseModel
# Create your models here.

STAR_CHOICES=[
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐')
    ]

class RatingAndReviewModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="feedback")
    advertise = models.ForeignKey(AdvertiseModel, on_delete=models.CASCADE,related_name="review")
    star = models.CharField(max_length=10, choices=STAR_CHOICES)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.advertise} {self.star}"
