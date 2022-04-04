from django import forms


class FormValidationError(Exception):
    pass


class PetsitterQuestion(forms.Form):
    is_petsitter = forms.BooleanField(
        required=False,
        label=(
            'Are you pet sitter / dog walker ?'
            ' If not, just leave this field blank.'
        ),
    )

    def save(self, user):
        if self.is_valid():
            user.is_petsitter = self.cleaned_data['is_petsitter']
            user.save()
            return user
        raise FormValidationError
