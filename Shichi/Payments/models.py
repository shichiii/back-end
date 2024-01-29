from django.db import models

# Create your models here.
class PaymentLog(models.Model):
    user_email = models.CharField(max_length=50)
    money = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    bank_code = models.CharField(max_length=50)
    was_successful = models.BooleanField(default=False)
    is_added = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add=True)