from django.db import models
from CustomAdvertisement.models import CustomAdvertisement
from CustomUser.models import CustomUser
class CustomHistories(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE , null=True, blank=True)
    advertisement = models.ForeignKey(CustomAdvertisement, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    take_or_own = models.CharField(default="take", blank=False)