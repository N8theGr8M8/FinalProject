from django import forms
from .models import EventData
class ProductForm(forms.ModelForm):
    class Meta:
        model = EventData
        fields = '__all__'
