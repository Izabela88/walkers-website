from django.db import models
from walker_profile.models import WalkerUser


class PetsitterReview(models.Model):
    TYPE_SELECT = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    user = models.ForeignKey(
        WalkerUser, on_delete=models.CASCADE, null=False, related_name="user_reviews"
    )
    reviewer = models.ForeignKey(
        WalkerUser, on_delete=models.CASCADE, null=False, related_name="reviewer_reviews"
    )
    description = models.TextField(blank=True, null=True)
    stars = models.IntegerField(choices=TYPE_SELECT, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_visible = models.BooleanField(null=False, default=False)
    is_admin_approved = models.BooleanField(null=False, default=False)