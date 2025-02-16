from django import forms
from .models import MenuItem, Menu

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'menu', 'is_vegetarian']

class MenuUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['price']