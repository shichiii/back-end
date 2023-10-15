from django.db import models
from CustomUser.models import CustomUser
from CustomCarImage.models import CustomCarImage
# Create your models here.
class CustomCar(models.Model):
    owner = models.ForeignKey(CustomUser)
    images = models.ManyToManyField(CustomCarImage)
    name = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=30, blank=True)
    producted_date = models.DateField()
    CATEGORIES = (
        ('economy', 'economy'),
        ('luxury', 'luxury'),
        ('compact', 'compact'), 
        ('offroad', 'offroad'),
        ('hybrid', 'hybrid'),
        ('electric', 'electic'),
        ('truck', 'truck'),
        ('convertible', 'convertible'), 
        ('passenger-van', 'passenger-van'), 
        ('mini-van', 'mini-van'),
        ('others', 'others'),   
    )
    category = models.CharField(max_length=20, choices=CATEGORIES, default='others')
    description = models.TextField(null=True, blank=True)