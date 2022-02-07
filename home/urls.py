"""
URL patterns for Home application
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("question", views.register_question, name="question"),
]