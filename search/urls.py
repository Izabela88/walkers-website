from django.urls import path
from . import views


urlpatterns = [
    path("petsitters_list", views.petsitters_list, name="petsitters_list"),
]