from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Locations(models.Model):
    name_location = models.CharField(max_length = 255)
    user = models.ForeignKey(User,on_delete = models.CASCADE)

class Devices(models.Model):
    name_device = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    location= models.ForeignKey(Locations,on_delete=models.CASCADE)

class Dots(models.Model):
    value=models.FloatField()
    dateTime=models.DateTimeField(auto_now_add=True)
    device= models.ForeignKey(Devices,on_delete=models.CASCADE)
