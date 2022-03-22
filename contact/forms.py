from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'maxlength': '100',

            }
        ),
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'maxlength': '100',
            }
        ),
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'rev-description',
                'rows': 4,
                'maxlength': '1500',
                'placeholder': 'write your message here...'

            }
        ),
    )