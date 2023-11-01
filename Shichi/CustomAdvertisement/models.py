from django.db import models
from CustomCarImage.models import CustomCarImage
from CustomAdvertisementLocation.models import CustomAdvertisementLocation
# Create your models here.
from CustomUser.models import CustomUser
class CustomAdvertisement(models.Model):
    owner_id = models.IntegerField(null=False, blank=False)
    location = models.ForeignKey(CustomAdvertisementLocation, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(null=True, blank=True)
       
    car_images = models.ManyToManyField(CustomCarImage)
    car_name = models.CharField(max_length=30, blank=True)
    car_color = models.CharField(max_length=30, blank=True)
    car_producted_date = models.DateField()
    CAR_CATEGORIES = (
        ('economy', 'economy'),
        ('luxury', 'luxury'),
        ('compact', 'compact'), 
        ('offroad', 'offroad'),
        ('hybrid', 'hybrid'),
        ('electric', 'electric'),
        ('truck', 'truck'),
        ('convertible', 'convertible'), 
        ('passenger-van', 'passenger-van'), 
        ('mini-van', 'mini-van'),
        ('others', 'others'),   
    )
    car_category = models.CharField(max_length=20, choices=CAR_CATEGORIES, default='others')
    
    
class Comment(models.Model):
    adv = models.ForeignKey(CustomAdvertisement, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments_adv')
    created_date = models.DateField(auto_now_add=True)
    text = models.TextField()
    def __str__(self):
        return f"{self.adv.car_name} {self.user.first_name}"
    def is_owner(self, user):
        return self.user == user
        