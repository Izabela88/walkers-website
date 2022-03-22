"""
URL patterns for Home application
"""

from django.urls import path
from contact.views import Contact


urlpatterns = [
    path("", Contact.as_view(), name="contact"),
    
]