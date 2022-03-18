from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from walker_profile.views import UserProfileView, WalkerUserReviewList, WalkerUserReview


urlpatterns = [
    path('user_profile/<int:id>', UserProfileView.as_view(), name='user_profile'),
    path('user_profile/<int:id>/reviews', WalkerUserReviewList.as_view(), name='reviews'),
    path('user_profile/<int:user_id>/reviews/<int:review_id>', WalkerUserReview.as_view(), name='walker_user_review'),
    ]
