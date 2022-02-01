from email.policy import default
from allauth.account.forms import SignupForm
from django import forms
from user.models import WalkerProfile


class ExtendedSignupForm(SignupForm):
    is_petsitter = forms.BooleanField(required=False,label='Mark the box below if you are a pet sitter/dog walker')
    def save(self, request):
        user = super(ExtendedSignupForm, self).save(request)
        user.save()
        walker_profile = WalkerProfile()
        walker_profile.is_petsitter = self.cleaned_data['is_petsitter']
        walker_profile.user = user
        walker_profile.save()
        return user
