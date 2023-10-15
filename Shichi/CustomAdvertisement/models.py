from django.db import models
from CustomUser.models import CustomUser
from CustomCar.models import CustomCar
from CustomAdvertisementLocation.models import CustomAdvertisementLocation
# Create your models here.

class CustomAdvertisement(models.Model):
    owner = models.ForeignKey(CustomUser)
    location = models.ForeignKey(CustomAdvertisementLocation)
    car = models.ForeignKey(CustomCar)
    name = models.CharField(max_length=30, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(null=True, blank=True)
    