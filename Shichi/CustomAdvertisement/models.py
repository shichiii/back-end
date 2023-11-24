from django.db import models
from CustomCarImage.models import CustomCarImage
from CustomAdvertisementLocation.models import CustomAdvertisementLocation
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CustomAdvertisement(models.Model):
    owner_id = models.IntegerField(null=False, blank=False)
    location = models.ForeignKey(CustomAdvertisementLocation, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(null=True, blank=True)
    car_image2 = models.ImageField(upload_to='car_images2/', blank=True)  
    car_images = models.ManyToManyField(CustomCarImage)
    car_name = models.CharField(max_length=30, blank=True)
    CAR_COLOR = (
        ('black', 'black'),
        ('white', 'white'),
        ('gray', 'gray'), 
        ('brown', 'brown'),
        ('navy-blue', 'navy-blue'),
        ('others', 'others'),   
    )
    car_color = models.CharField(max_length=20, choices=CAR_COLOR, default='others')
    car_produced_date = models.DateField()
    car_seat_count = models.IntegerField(null=True, blank=True)
    car_door_count = models.IntegerField(null=True, blank=True)
    car_Is_cooler = models.BooleanField(default=False)
    CAR_GEARBOX = (
        ('manual', 'manual'),
        ('automatic', 'automatic'),
    )
    car_gearbox = models.CharField(max_length=20, choices=CAR_GEARBOX, default='manual')
    car_fuel = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
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
    user_id = models.IntegerField(null=False, blank=False)
    created_date = models.DateField(auto_now_add=True)
    text = models.TextField()
    def __str__(self):
        return f"{self.adv.car_name} {self.text}"
    def is_owner(self, user):
        return self.user == user
    
class Rate(models.Model):
    adv = models.ForeignKey(CustomAdvertisement, on_delete=models.CASCADE, related_name='rates')
    user_id = models.IntegerField(null=False, blank=False)
    rate = models.DecimalField(
        max_digits=2, decimal_places=1, default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __str__(self):
        return f"rated {self.rate} to {self.adv.car_name}"