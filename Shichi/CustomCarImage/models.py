from django.db import models

# Create your models here.

class CustomCarImage(models.Model):
    image = models.ImageField(upload_to='car_images/', blank=True)