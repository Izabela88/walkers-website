from django.db import models
from walker_profile.models import WalkerUser

class PetsitterReview(models.Model):
    user = models.ForeignKey(
        WalkerUser, on_delete=models.CASCADE, null=False, related_name="user"
    )
    reviewer = models.ForeignKey(
        WalkerUser, on_delete=models.CASCADE, null=False, related_name="reviewer"
    )
    description = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_visible = models.BooleanField(null=True)
    is_admin_approved = models.BooleanField(null=False)