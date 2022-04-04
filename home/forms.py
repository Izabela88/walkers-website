from django import forms


class PetsitterFormValidationError(Exception):
    """Raised when Petsitter form is invalid"""

    pass


class PetsitterQuestionForm(forms.Form):
    is_petsitter = forms.BooleanField(
        required=False,
        label=(
            'Mark the field if you want to register as the pet sitter / '
            ' dog walker. If not, just leave this field blank.'
        ),
    )

    def save(self, user):
        """Save user instance with updated fields from form.

        Args:
            user (User): Django User object

        Raises:
            PetsitterFormValidationError: Raises in case form is invalid

        Returns:
            User: Updated user
        """
        if self.is_valid():
            user.is_petsitter = self.cleaned_data['is_petsitter']
            user.save()
            return user
        raise PetsitterFormValidationError
