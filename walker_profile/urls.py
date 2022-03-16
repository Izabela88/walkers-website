from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from walker_profile.views import UserProfileView, ReviewList


urlpatterns = [
    path('user_profile/<int:id>', UserProfileView.as_view(), name='user_profile'),
    path('user_profile/<int:id>/reviews', ReviewList.as_view(), name='reviews'),
    ]
