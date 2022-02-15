from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# from django.db.models.signals import post_save
# from django.dispatch import receiver


class WalkerUser(AbstractUser):
    address_details = models.OneToOneField('AddressDetails', null=True, on_delete=models.CASCADE)
    is_petsitter = models.BooleanField(null=True)
    username = models.CharField(max_length=150, null=True, unique=False)
    phone_number = PhoneNumberField(null=True, blank=False, unique=True)

    def __str__(self):
        return str(self.username)


class AddressDetails(models.Model):
    town = models.CharField(max_length=200, null=True)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    postcode = models.CharField(max_length=200, null=True)
  



# @receiver(post_save, sender=WalkerUser)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         WalkerUser.objects.create(user=instance)

# @receiver(post_save, sender=WalkerUser)
# def save_profile(sender, instance, **kwargs):
#     instance.user.save()