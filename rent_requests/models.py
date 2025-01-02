from django.db import models
from django.contrib.auth.models import User
from advertise.models import Ad
# Create your models here.

class Request(models.Model):
      ad=models.ForeignKey(Ad,on_delete=models.CASCADE)
      renter=models.ForeignKey(User,on_delete=models.CASCADE)
      is_accepted=models.BooleanField(default=False)
      
      def __str__(self):
          return f'Request from {self.renter} for ad {self.ad}'