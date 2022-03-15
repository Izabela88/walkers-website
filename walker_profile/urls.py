from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from walker_profile.views import UserProfileView, MyReview




urlpatterns = [
    path('user_profile/<int:id>', UserProfileView.as_view(), name='user_profile'),
    path('user_profile/<int:id>/my_reviews', MyReview.as_view(), name='my_reviews'),
    ]
