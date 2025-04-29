from django import forms
from .models import Car, Service, Transaction

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'base_price']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['date', 'description', 'cost']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['is_loan', 'down_payment', 'tenor', 'annual_interest_rate']