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
        fields = ['is_loan', 'annual_interest_rate', 'total_cost']

    def save(self, commit=True):
        transaction = super().save(commit=False)

        if commit:
            transaction.save()

            if self.cleaned_data.get('car_sold', False):
                car = transaction.car
                car.is_sold = True
                car.save()
            
        return transaction
