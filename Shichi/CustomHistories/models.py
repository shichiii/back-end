from django.db import models
from CustomAdvertisement.models import CustomAdvertisement
# Create your models here.

class CustomHistories(models.Model):
    advertisement = models.ForeignKey(CustomAdvertisement)
    created_date = models.DateTimeField(auto_now_add=True)
    