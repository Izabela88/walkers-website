from django import forms
from walker_profile.models import WalkerUser

class FormValidationError(Exception):
    pass


class PetsitterQuestion(forms.Form):
    is_petsitter = forms.BooleanField(required=False, label='Please mark field below only if you are the pet sitter / dog walker')
    def save(self, user):
        if self.is_valid():
            user = WalkerUser()
            user.is_petsitter = self.cleaned_data['is_petsitter']
            user.save()
            return user
        raise FormValidationError