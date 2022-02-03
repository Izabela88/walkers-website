from django import forms
from user.models import WalkerProfile

class FormValidationError(Exception):
    pass


class PetsitterQuestion(forms.Form):
    is_petsitter_social = forms.BooleanField(required=False, label='Please mark field below only if you are the pet sitter / dog walker')
    def save(self, user):
        if self.is_valid():
            walker_profile = WalkerProfile()
            walker_profile.is_petsitter = self.cleaned_data['is_petsitter_social']
            walker_profile.user = user
            walker_profile.save()
            return user
        raise FormValidationError