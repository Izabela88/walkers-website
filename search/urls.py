from django.urls import path
from search.views import SearchView, PetsitterProfile


urlpatterns = [
    path('petsitters_list', SearchView.as_view(), name='petsitters_list'),  
    path('petsitter_profile/<int:id>', PetsitterProfile.as_view(), name='petsitter_profile'),  
]