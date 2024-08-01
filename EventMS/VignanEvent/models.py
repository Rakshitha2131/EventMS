from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
 
class EventModel(models.Model):
    Event_name = models.CharField(max_length = 255)
    date = models.DateField()
    venue_name = models.CharField(max_length = 255) 
