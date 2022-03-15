"""
URL patterns for Home application
"""

from django.urls import path
from . import views
from reviews.views import Review
from search.views import SearchView, PetsitterProfile


urlpatterns = [
   path(
        'petsitter_profiles/<int:id>',
        PetsitterProfile.as_view(),
        name='petsitter_profile',
    ),
    path(
    'petsitter_profiles/<int:id>/review',
    Review.as_view(),
    name='reviews',
    ),
    
]