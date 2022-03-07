"""
URL patterns for Home application
"""

from django.urls import path
from . import views
from reviews.views import Review

urlpatterns = [
    path(
    '<int:id>',
    Review.as_view(),
    name='reviews',
    ),   
]