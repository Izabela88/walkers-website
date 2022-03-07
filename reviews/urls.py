"""
URL patterns for Home application
"""

from django.urls import path
from . import views


urlpatterns = [
    path("reviews", views.reviews, name="reviews"),
]