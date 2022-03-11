from django import forms
from reviews.models import PetsitterReview
from django.core.validators import MaxValueValidator, MinValueValidator


class PetsitterReviewForm(forms.Form):
    TYPE_SELECT = (
        ('0', '☆'),
        ('1', '☆'),
        ('2', '☆'),
        ('3', '☆'),
        ('4', '☆'),
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'rev-description',
                'rows': 4,
                'maxlength': '1500',
                'style': 'resize:none',

            }
        ),
    ) 
    stars = forms.ChoiceField(choices=TYPE_SELECT, widget=forms.RadioSelect())

    class Meta:
        model = PetsitterReview
        fields = [
            'description',
            'stars'
        ]