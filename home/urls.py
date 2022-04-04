"""
URL patterns for Home application
"""

from django.urls import path
from home.views import Home, RegisterQuestion


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("question", RegisterQuestion.as_view(), name="question"),
]
