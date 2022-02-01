from django.db import models
from django.contrib.auth.models import User


class WalkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_petsitter = models.BooleanField()