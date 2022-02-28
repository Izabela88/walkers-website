"""
URL patterns for Home application
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("question", views.register_question, name="question"),
    path("petsitters_list", views.petsitters_list, name="petsitters_list"),
]