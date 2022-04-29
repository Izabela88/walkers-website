from django import forms
from contact.utility import send_email
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.validators import validate_email


class ContactForm(forms.Form):
    """App contact message form"""

    only_letters = RegexValidator(
        (
            "^[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
            "a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ"
            "a-zA-ZäöüßÄÖÜ"
            "a-zA-ZàèéìíîòóùúÀÈÉÌÍÎÒÓÙÚ"
            "a-zA-ZáéíñóúüÁÉÍÑÓÚÜ"
            "a-zA-ZäöåÄÖÅ"
            "a-zA-ZæøåÆØÅ"
            "а-яА-ЯёЁ"
            "а-щА-ЩЬьЮюЯяЇїІіЄєҐґ"
            "А-ИК-ШЂЈ-ЋЏа-ик-шђј-ћџ"
            "а-ъьюяА-ЪЬЮЯ"
            "ёа-зй-шы-яЁА-ЗЙ-ШЫІіЎў"
            "a-zA-ZĂÂÎȘȚăâîșț ]*$"
        ),
        "No special characters and numbers allowed!",
    )

    full_name = forms.CharField(
        required=True,
        validators=[only_letters],
        widget=forms.TextInput(
            attrs={
                "maxlength": "100",
            }
        ),
    )
    email = forms.EmailField(
        validators=[validate_email],
        required=True,
        widget=forms.EmailInput(
            attrs={
                "maxlength": "254",
            }
        ),
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "rev-description",
                "rows": 4,
                "maxlength": "1500",
                "placeholder": "write your message here...",
            }
        ),
    )

    def submit_email(self) -> bool:
        """Submit email wrapper. Method will pass `send_email` response and it
        will inject required email arguments

        Returns:
            bool: True if email sent successfully, else False
        """
        return send_email(
            [settings.EMAIL_HOST_USER],
            self.cleaned_data["email"],
            self.format_message(),
            "You got a mail!",
        )

    def format_message(self) -> str:
        """Format email message

        Returns:
            str: Formatted email message
        """
        message = """
            From:\n\t\t{}\n
            Email:\n\t\t{}\n
            Message:\n\t\t{}\n""".format(
            self.cleaned_data["full_name"],
            self.cleaned_data["email"],
            self.cleaned_data["message"],
        )
        return message
