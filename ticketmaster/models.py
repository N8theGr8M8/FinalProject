from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class EventData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, blank=True, default='')
    image = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    date = models.CharField(max_length=255)

