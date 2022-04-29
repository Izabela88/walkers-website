from django import forms
from newsletter.models import NewsletterUser
from django.core.validators import validate_email


class NewsletterUserForm(forms.ModelForm):
    newsletter_email = forms.CharField(
        required=True,
        validators=[validate_email],
        widget=forms.EmailInput(
            attrs={
                "maxlength": "254",
                "placeholder": "write your email here...",
                "class": "newsletter-input",
            }
        ),
    )

    class Meta:
        model = NewsletterUser
        fields = [
            "newsletter_email",
        ]
