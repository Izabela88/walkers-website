
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from walker_profile.views import UserProfileView





urlpatterns = [
    path('user_profile', UserProfileView.as_view(), name='user_profile')


    
]
