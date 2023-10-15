from django.db import models

# Create your models here.

class CustomAdvertisementLocation(models.Model):
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    geo_width = models.CharField(max_length=30, blank=True)
    geo_length = models.CharField(max_length=30, blank=True)
    
    