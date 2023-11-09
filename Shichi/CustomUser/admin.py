from django.contrib import admin
from .models import CustomUser, Wallet

admin.site.register(CustomUser)
admin.site.register(Wallet)
