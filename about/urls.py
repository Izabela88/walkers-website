"""
URL patterns for About application
"""

from django.urls import path
from about.views import AboutView


urlpatterns = [
    path("", AboutView.as_view(), name="about"),
]
