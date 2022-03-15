from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from walker_profile.views import UserProfileView, MyReviews



urlpatterns = [
    path('user_profile', UserProfileView.as_view(), name='user_profile'),
    path('user_profile/my_reviews', MyReviews.as_view(), name='my_reviews'),
    ]
