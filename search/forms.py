from django import forms

CARE_TYPE = [
    ('boarding_at_petsitter_home', 'Boarding at petsitter home'),
    ('boarding_at_client_home', 'Boarding at my home'),
    ('walk', 'Walking in my neighborhood'),
    ]

    
DOG_SIZE = [
    ('small', 'Small (> 10kg)'),
    ('medium', 'Medium (10 - 20kg)'),
    ('big', 'Big  (< 20kg)'),
    ]


AREA = [
    ('close', '> 5 miles'),
    ('medium', '10 miles'),
    ('far', '15 miles'),
    ]


class SearchForm(forms.Form):
    post_code= forms.CharField(max_length=8, required=True)
    care_type= forms.CharField(label='Care Type:', widget=forms.Select(choices=CARE_TYPE))
    dog_size= forms.CharField(label='My Dog Size:', widget=forms.Select(choices=DOG_SIZE))
    area= forms.CharField(label='Location:', widget=forms.Select(choices=AREA))

