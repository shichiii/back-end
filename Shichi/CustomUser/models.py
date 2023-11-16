from django.db import models
from CustomHistories.models import CustomHistories
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
# from django.contrib.auth.models import (PermissionsMixin , AbstractBaseUser ,  UserManager)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        email = self.normalize_email(email)
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)
  

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    history = models.ForeignKey(CustomHistories, on_delete=models.CASCADE, null=True, blank=True)
    #############################################################################
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
    #############################################################################
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    def __str__(self):
        return self.email