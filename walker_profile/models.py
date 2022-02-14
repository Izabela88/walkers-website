from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


# from django.db.models.signals import post_save
# from django.dispatch import receiver


class WalkerUser(AbstractUser):
    contact_details = models.OneToOneField('ContactDetails', null=True, on_delete=models.CASCADE)
    is_petsitter = models.BooleanField(null=True)
    username = models.CharField(max_length=150, null=True, unique=False)

    def __str__(self):
        return str(self.username)


class ContactDetails(models.Model):
    numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')

    first_name = models.CharField(max_length=50, null=True, validators=[numeric])
    last_name = models.CharField(max_length=50, null=True, validators=[numeric])
    email = models.EmailField(max_length=200, null=True, unique=True)
    town = models.CharField(max_length=200, null=True, validators=[numeric])
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    postcode = models.CharField(max_length=200, null=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)



# @receiver(post_save, sender=WalkerUser)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         WalkerUser.objects.create(user=instance)

# @receiver(post_save, sender=WalkerUser)
# def save_profile(sender, instance, **kwargs):
#     instance.user.save()