from django.db import models


class NewsletterUser(models.Model):
    email = models.EmailField(null=False, blank=False, primary_key=True)
    is_subscribed = models.BooleanField(null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    unsubscribed_at = models.DateTimeField(null=True)
