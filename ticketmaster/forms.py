from django import forms
from .models import EventData


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = EventData
        exclude = ['user']
