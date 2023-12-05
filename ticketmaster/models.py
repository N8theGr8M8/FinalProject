from django.db import models


#Create your models here.
class EventData(models.Model):
    name = models.CharField(max_length=255)
    # image = models.CharField(max_length=255)
    # startDate = models.DateField
    # startTime = models.DateTimeField
    # venueName = models.CharField(max_length=55)
    # venueAddress = models.CharField(max_length=55)
    # venueCity = models.CharField(max_length=55)
    # venueState = models.CharField(max_length=55)
    # link = models.ImageField

