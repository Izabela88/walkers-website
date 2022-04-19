from django.contrib.auth.models import User
from allauth.account.utils import perform_login
from django.dispatch import receiver
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

# https://stackoverflow.com/questions/28897220/django-allauth-social
# -account-connect-to-existing-account-on-login
class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if user.id:
            return
        try:
            """
            if user exists, connect the account to the existing account and
            login
            """
            walker_user = get_user_model().objects.get(email=user.email)
            sociallogin.state["process"] = "connect"
            perform_login(request, walker_user, email_verification="mandatory")
        except get_user_model().DoesNotExist:
            pass
