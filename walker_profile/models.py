from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib import messages


# from django.db.models.signals import post_save
# from django.dispatch import receiver


class WalkerUser(AbstractUser):
    address_details = models.OneToOneField('AddressDetails', null=True, on_delete=models.CASCADE)
    is_petsitter = models.BooleanField(null=True)
    username = models.CharField(max_length=150, null=True, unique=False)
    phone_number = PhoneNumberField(null=True, blank=False, unique=True)
    avatar = models.ImageField(null=True, blank=True)

    def delete(self, *args, **kwargs):
        if self.avatar:         
            storage, path = self.avatar.storage, self.avatar.path     
            storage.delete(path)    
        super(WalkerUser, self).delete(*args, **kwargs)


    def __str__(self):
        return str(self.username)


class AddressDetails(models.Model):
    address = models.CharField(verbose_name='Address', max_length=100, null=True)
    address_1 = models.CharField(verbose_name='Address 1', max_length=100, null=True)
    address_2 = models.CharField(verbose_name='Address 2', max_length=100, null=True)
    town = models.CharField(verbose_name='Town/City', max_length=100, null=True)
    post_code = models.CharField(verbose_name='Post Code', max_length=8, null=True)
    county = models.CharField(verbose_name='County', max_length=100, null=True)
    country = models.CharField(verbose_name='Country', max_length=100, null=True)
    longtitude = models.CharField(verbose_name='Longtitude', max_length=50, null=True)
    latitude = models.CharField(verbose_name='Latitude', max_length=50, null=True)
    
  