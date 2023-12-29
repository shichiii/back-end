from django.db import models

class CustomDate(models.Model):
    date = models.DateField()
    adv_id = models.IntegerField(blank=False)