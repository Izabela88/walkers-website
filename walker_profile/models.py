from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class WalkerUser(AbstractUser):
    is_petsitter = models.BooleanField(null=True)
    username = models.CharField(max_length=150, null=True, unique=False)

    def __str__(self):
        return str(self.username)


# @receiver(post_save, sender=WalkerUser)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         WalkerUser.objects.create(user=instance)

# @receiver(post_save, sender=WalkerUser)
# def save_profile(sender, instance, **kwargs):
#     instance.user.save()