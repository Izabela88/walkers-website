from django.db import models
from django.contrib.auth.models import AbstractUser


class WalkerUser(AbstractUser):
    is_petsitter = models.BooleanField(null=True)
    phone_number = models.CharField(max_length=20, null=True)



