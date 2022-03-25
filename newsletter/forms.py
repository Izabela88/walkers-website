from django import forms
from newsletter.models import NewsletterUser

class NewsletterUserForm(forms.ModelForm):
    newsletter_email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'maxlength': '100',
                'placeholder': 'write your email here...',
                'class': 'newsletter-input'
            }
        ),
    )


    class Meta:
        model = NewsletterUser
        fields = [
            'newsletter_email',

        ]