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
        label=(
            "Mark the field below if you want to register as the "
            " pet sitter / dog walker.  If not, just leave it blank."
        ),
    )

    def save(self, request):
        user = super(ExtendedSignupForm, self).save(request)
        user.is_petsitter = self.cleaned_data["is_petsitter"]
        user.save()
        return user


class UpdateWalkerProfileForm(forms.ModelForm):

    only_letters = RegexValidator("^[a-zA-Z ]*$", "You can use only letters!")

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
            "phone_number",
            "email",
            "first_name",
            "last_name",
            "email",
        ]


class WalkerAddressForm(forms.ModelForm):
    address_1 = forms.CharField(max_length=50, required=True)
    address_2 = forms.CharField(max_length=100, required=True)
    town = forms.CharField(max_length=85, required=True)
    postcode = forms.CharField(max_length=8, required=True)
    county = forms.CharField(max_length=100, required=True)

    class Meta:
        model = AddressDetails
        fields = ["address_1", "address_2", "town", "postcode", "county"]


class WalkerUserAvatarForm(forms.ModelForm):

    avatar = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={"class": "form-control-file"}),
    )

    class Meta:
        model = WalkerUser
        fields = ["avatar"]


class PetsitterDescriptionForm(forms.ModelForm):
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4,
                "maxlength": "1500",
                "style": "resize:none",
            }
        ),
    )

    class Meta:
        model = PetsitterDetails
        fields = ["description"]


class ServiceDetailsForm(forms.ModelForm):
    is_active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "switch-input",
            }
        ),
    )
    is_small_dog = forms.BooleanField(
        required=False,
        label="Small Dog (< 10kg)",
        widget=forms.CheckboxInput(
            attrs={
                "class": "small-dog",
            }
        ),
    )
    is_medium_dog = forms.BooleanField(
        required=False,
        label="Medium Dog (10-20 kg)",
        widget=forms.CheckboxInput(
            attrs={
                "class": "medium-dog",
            }
        ),
    )
    is_big_dog = forms.BooleanField(
        required=False,
        label="Big Dog (> 20kg)",
        widget=forms.CheckboxInput(
            attrs={
                "class": "big-dog",
            }
        ),
    )
    s_price_hour = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "maxlength": "10",
                "placeholder": "£ per hour",
                "class": "price_hour_s",
            }
        ),
    )
    s_price_day = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "maxlength": "10",
                "placeholder": "£ per day",
                "class": "price_day_s",
            }
        ),
    )
    m_price_hour = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "maxlength": "10",
                "placeholder": "£ per hour",
                "class": "price_hour_m",
            }
        ),
    )
    m_price_day = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "maxlength": "10",
                "placeholder": "£ per day",
                "class": "price_day_m",
            }
        ),
    )
    b_price_hour = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "maxlength": "10",
                "placeholder": "£ per hour",
                "class": "price_hour_b",
            }
        ),
    )
    b_price_day = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "maxlength": "10",
                "placeholder": "£ per day",
                "class": "price_day_b",
            }
        ),
    )

    def clean(self):
        cleaned_data = super(ServiceDetailsForm, self).clean()
        is_small_dog = cleaned_data.get("is_small_dog")
        s_price_hour = cleaned_data.get("s_price_hour")
        s_price_day = cleaned_data.get("s_price_day")
        is_medium_dog = cleaned_data.get("is_medium_dog")
        m_price_hour = cleaned_data.get("m_price_hour")
        m_price_day = cleaned_data.get("m_price_day")
        is_big_dog = cleaned_data.get("is_big_dog")
        b_price_hour = cleaned_data.get("b_price_hour")
        b_price_day = cleaned_data.get("b_price_day")
        is_active = cleaned_data.get("is_active")
        if is_small_dog and (s_price_hour is None and s_price_day is None):
            raise forms.ValidationError(
                {"is_small_dog": "Please fill in at least one price field"}
            )
        if is_medium_dog and (m_price_hour is None and m_price_day is None):
            raise forms.ValidationError(
                {"is_medium_dog": "Please fill in at least one price field"}
            )
        if is_big_dog and (b_price_hour is None and b_price_day is None):
            raise forms.ValidationError(
                {"is_big_dog": "Please fill in at least one price field"}
            )

        if (
            is_active
            and not is_small_dog  # noqa: W503
            and not is_medium_dog  # noqa: W503
            and not is_big_dog  # noqa: W503
        ):
            raise forms.ValidationError(
                {"is_active": "You should mark at least one dog size option"}
            )
        return cleaned_data

    class Meta:
        model = ServiceDetails
        fields = [
            "is_active",
            "is_small_dog",
            "is_big_dog",
            "is_medium_dog",
            "s_price_hour",
            "s_price_day",
            "m_price_hour",
            "m_price_day",
            "b_price_hour",
            "b_price_day",
        ]
