from allauth.account.forms import SignupForm
from django import forms
from walker_profile.models import WalkerUser, AddressDetails
from django.core.validators import RegexValidator



class ExtendedSignupForm(SignupForm):
    is_petsitter = forms.BooleanField(required=False,label='Mark the box only if you are a pet sitter/dog walker')
    def save(self, request):
        user = super(ExtendedSignupForm, self).save(request)
        user.is_petsitter = self.cleaned_data['is_petsitter']        
        user.save()
        return user


class UpdateWalkerProfile(forms.ModelForm):

    only_letters = RegexValidator("^[a-zA-Z ]*$", 'You can use only letters!')

    first_name = forms.CharField(max_length=100, required=True, validators=[only_letters])
    last_name = forms.CharField(max_length=100, required=True, validators=[only_letters])
    email = forms.EmailField(required=True)


    class Meta:
        model = WalkerUser
        fields = ['phone_number', 'email', 'first_name', 'last_name']


class WalkerAddressForm(forms.ModelForm):
    address_1 = forms.CharField(max_length=50, required=True)
    address_2 = forms.CharField(max_length=100, required=True)
    town = forms.CharField(max_length=85, required=True)
    post_code = forms.CharField(max_length=8, required=True)
    county = forms.CharField(max_length=100, required=True)
    class Meta:
        model = AddressDetails
        fields = ['address_1', 'address_2', 'town', 'post_code', 'county']