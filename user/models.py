from django.db import models
from django.contrib.auth.models import User

class PetsitterAttrError(Exception):
    """Raise when user is missing user_walkerprofile entry"""
    pass


class WalkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_petsitter = models.BooleanField()


def is_petsitter(self):
    try:
        return self.walkerprofile.is_petsitter
    except AttributeError:
        raise PetsitterAttrError

User.add_to_class("is_petsitter", is_petsitter)