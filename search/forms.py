from django import forms

CARE_TYPE = [
    ("boarding_at_pet_sitter_home", "Boarding at pet sitter home"),
    ("day_care_at_client_home", "Day care at my home"),
    ("walk", "Walking in my neighborhood"),
]


DOG_SIZE = [
    ("small", "Small (< 10kg)"),
    ("medium", "Medium (10 - 20kg)"),
    ("big", "Big  (> 20kg)"),
]


AREA = [
    (5, "< 5 miles"),
    (10, "10 miles"),
    (15, "15 miles"),
    (20, "20 miles"),
]


class SearchForm(forms.Form):
    postcode = forms.CharField(max_length=8, required=True)
    care_type = forms.CharField(
        label="Care Type:", widget=forms.Select(choices=CARE_TYPE)
    )
    dog_size = forms.CharField(
        label="My Dog Size:", widget=forms.Select(choices=DOG_SIZE)
    )
    area = forms.CharField(
        label="Location:", widget=forms.Select(choices=AREA)
    )
