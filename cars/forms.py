from django import forms
from .models import Car, Service

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'base_price']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['date', 'description', 'cost']