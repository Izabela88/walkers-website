from django.urls import path
from newsletter.views import Newsletter

urlpatterns = [
    path("", Newsletter.as_view(), name="newsletter"),
]
