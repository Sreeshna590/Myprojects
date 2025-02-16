from django import forms
from app1.models import School

class SchoolForm(forms.ModelForm):
    location_choices = [
        ('ernakulam', 'Ernakulam'),
        ('trivandrum', 'Trivandrum'),
        ('kollam', 'Kollam')
    ]
    location = forms.ChoiceField(
        choices=location_choices,
        widget=forms.Select,
        required=True
    )

    class Meta:
        model = School
        fields = ['name', 'location', 'principal']
