"""
URL patterns for Home application
"""

from django.urls import path
from . import views
from reviews.views import Review
from search.views import SearchView, PetsitterProfile


urlpatterns = [
    path(
    '<int:id>',
    Review.as_view(),
    name='reviews',
    ),
   path(
        'petsitter_profiles/<int:id>',
        PetsitterProfile.as_view(),
        name='petsitter_profile',
    ),
]