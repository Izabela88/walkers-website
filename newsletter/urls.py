from django.urls import path
from newsletter.views import Newsletter, UpdateSubscription


urlpatterns = [
    path("", Newsletter.as_view(), name="newsletter"),
    path("update", UpdateSubscription.as_view(), name="update_subscription"),
]
