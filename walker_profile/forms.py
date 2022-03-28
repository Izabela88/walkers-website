from allauth.account.forms import SignupForm
from django import forms
from walker_profile.models import (
    WalkerUser,
    AddressDetails,
    PetsitterDetails,
    ServiceDetails,
)
from django.core.validators import RegexValidator


class ExtendedSignupForm(SignupForm):
    is_petsitter = forms.BooleanField(
        required=False,
        label='Mark the box only if you are a pet sitter/dog walker',
    )

    def save(self, request):
        user = super(ExtendedSignupForm, self).save(request)
        user.is_petsitter = self.cleaned_data['is_petsitter']
        user.save()
        return user


class UpdateWalkerProfileForm(forms.ModelForm):

    only_letters = RegexValidator("^[a-zA-Z ]*$", 'You can use only letters!')

    first_name = forms.CharField(
        max_length=100, required=True, validators=[only_letters]
    )
    last_name = forms.CharField(
        max_length=100, required=True, validators=[only_letters]
    )
    email = forms.EmailField(required=True)

    class Meta:
        model = WalkerUser
        fields = [
            'phone_number',
            'email',
            'first_name',
            'last_name',
            'email',
        ]


class WalkerAddressForm(forms.ModelForm):
    address_1 = forms.CharField(max_length=50, required=True)
    address_2 = forms.CharField(max_length=100, required=True)
    town = forms.CharField(max_length=85, required=True)
    postcode = forms.CharField(max_length=8, required=True)
    county = forms.CharField(max_length=100, required=True)

    class Meta:
        model = AddressDetails
        fields = ['address_1', 'address_2', 'town', 'postcode', 'county']


class WalkerUserAvatarForm(forms.ModelForm):

    avatar = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={'class': 'form-control-file'}),
    )

    class Meta:
        model = WalkerUser
        fields = ['avatar']


class PetsitterDescriptionForm(forms.ModelForm):
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4,
                'maxlength': '1500',
                'style': 'resize:none',
            }
        ),
    )

    class Meta:
        model = PetsitterDetails
        fields = ['description']


class ServiceDetailsForm(forms.ModelForm):
    is_active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'switch-input',
            }
        ),
    )
    is_small_dog = forms.BooleanField(
        required=False, label='Small Dog (< 10kg)'
    )
    is_medium_dog = forms.BooleanField(
        required=False, label='Medium Dog (10-20 kg)'
    )
    is_big_dog = forms.BooleanField(required=False, label='Big Dog (> 20kg)')
    s_price_hour = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'maxlength': '10', 'placeholder': '£ per hour'}
        ),
    )
    s_price_day = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'maxlength': '10', 'placeholder': '£ per day'}
        ),
    )
    m_price_hour = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'maxlength': '10', 'placeholder': '£ per hour'}
        ),
    )
    m_price_day = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'maxlength': '10', 'placeholder': '£ per day'}
        ),
    )
    b_price_hour = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'maxlength': '10', 'placeholder': '£ per hour'}
        ),
    )
    b_price_day = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'maxlength': '10', 'placeholder': '£ per day'}
        ),
    )

    class Meta:
        model = ServiceDetails
        fields = [
            'is_active',
            'is_small_dog',
            'is_big_dog',
            'is_medium_dog',
            's_price_hour',
            's_price_day',
            'm_price_hour',
            'm_price_day',
            'b_price_hour',
            'b_price_day',
        ]
