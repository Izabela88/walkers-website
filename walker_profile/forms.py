from tkinter import Place
from allauth.account.forms import SignupForm
from django import forms



class ExtendedSignupForm(SignupForm):
    is_petsitter = forms.BooleanField(required=False,label='Mark the box only if you are a pet sitter/dog walker')
    def save(self, request):
        user = super(ExtendedSignupForm, self).save(request)
        user.is_petsitter = self.cleaned_data['is_petsitter']        
        user.save()
        return user
