from tkinter import Place
from allauth.account.forms import SignupForm
from django import forms



class ExtendedSignupForm(SignupForm):
    is_petsitter = forms.BooleanField(required=False,label='Mark the box only if you are a pet sitter/dog walker')
    phone = forms.CharField(max_length=12, label='Phone number')
    def save(self, request):
        user = super(ExtendedSignupForm, self).save(request)
        user.is_petsitter = self.cleaned_data['is_petsitter']        
        user.phone_number = self.cleaned_data['phone']
        user.save()
        return user



# class UserContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactDetails
#         fields = ['first_name', 'last_name', 'email', 'address_1', 'address_2', 'town', 'postcode', 'phone_number']
