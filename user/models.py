from django.db import models
from django.contrib.auth.models import User



class WalkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_petsitter = models.BooleanField()


def is_petsitter(self):
    if hasattr(self, 'walkerprofile'):
        return self.walkerprofile.is_petsitter
    return False

User.add_to_class("is_petsitter",is_petsitter)