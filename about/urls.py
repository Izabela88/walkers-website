"""
URL patterns for About application
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.about, name="about"),

]