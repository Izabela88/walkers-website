from allauth.account.forms import SignupForm
from django import forms
from walker_profile.models import WalkerUser
from phonenumber_field.modelfields import PhoneNumberField



class ExtendedSignupForm(SignupForm):
    is_petsitter = forms.BooleanField(required=False,label='Mark the box only if you are a pet sitter/dog walker')
    def save(self, request):
        user = super(ExtendedSignupForm, self).save(request)
        user.is_petsitter = self.cleaned_data['is_petsitter']        
        user.save()
        return user


class UpdateWalkerProfile(forms.ModelForm):

    first_name = forms.CharField(max_length=100,
                               required=True,
    )
    last_name = forms.CharField(max_length=100,
                               required=True,
    )

    email = forms.EmailField(required=True,
    )


    class Meta:
        model = WalkerUser
        fields = ['phone_number', 'email', 'first_name', 'last_name']