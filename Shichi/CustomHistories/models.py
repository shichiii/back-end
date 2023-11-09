from django.db import models
from CustomAdvertisement.models import CustomAdvertisement

class CustomHistories(models.Model):
    advertisement = models.ForeignKey(CustomAdvertisement, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    take_or_own = models.CharField(default="take", blank=False)