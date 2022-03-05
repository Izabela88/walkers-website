from statistics import mode
from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError


class WalkerUser(AbstractUser):
    # https://stackoverflow.com/questions/6195478/max-image-size-on-file-upload
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 0.4
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Image is too big. Max file size is %sMB" % str(megabyte_limit))

    address_details = models.OneToOneField('AddressDetails', null=True, on_delete=models.CASCADE)
    petsitter_details = models.OneToOneField('PetsitterDetails', null=True, on_delete=models.CASCADE)
    is_petsitter = models.BooleanField(null=True)
    username = models.CharField(max_length=150, null=True, unique=False)
    phone_number = PhoneNumberField(null=True, blank=False, unique=True)
    avatar = models.ImageField(upload_to='avatar_images/', null=True, blank=True, validators=[validate_image])

    def delete(self, *args, **kwargs):
        if self.avatar:         
            storage, path = self.avatar.storage, self.avatar.path     
            storage.delete(path)    
        super(WalkerUser, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        try:
            this = WalkerUser.objects.get(id=self.id)
            if this.avatar != self.avatar:
                this.avatar.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)

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
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)


class PetsitterDetails(models.Model):
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

class ServiceTypes(models.Model):
    types = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class ServiceDetails(models.Model):
    user = models.ForeignKey(WalkerUser, on_delete=models.CASCADE, null=False, related_name="service_details")
    service_type = models.ForeignKey(ServiceTypes, on_delete=models.CASCADE, null=False)
    is_active = models.BooleanField(null=True)
    is_small_dog = models.BooleanField(null=True)
    s_price_hour = models.CharField(max_length=10, null=True)
    s_price_day = models.CharField(max_length=10, null=True)
    is_medium_dog = models.BooleanField(null=True)
    m_price_hour = models.CharField(max_length=10, null=True)
    m_price_day = models.CharField(max_length=10, null=True)
    is_big_dog = models.BooleanField(null=True)
    b_price_hour = models.CharField(max_length=10, null=True)
    b_price_day = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)


