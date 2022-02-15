"""
URL patterns for Home application
"""

from django.urls import path
from . import views


urlpatterns = [
    path("user_profile", views.user_profile, name="user_profile"),
    path("update_walker_profile", views.update_walker_profile, name="update_walker_profile"),
]