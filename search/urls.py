from django.urls import path
from search.views import SearchView, PetsitterProfile


urlpatterns = [
    path(
        'petsitter_profiles', SearchView.as_view(), name='petsitter_profiles'
    ),
    path(
        'petsitter_profiles/<int:id>',
        PetsitterProfile.as_view(),
        name='petsitter_profiles',
    ),
]
