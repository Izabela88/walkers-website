from django.urls import path
from . import views
from newsletter.views import Newsletter

urlpatterns = [
    path("", Newsletter.as_view(), name="newsletter"),
]