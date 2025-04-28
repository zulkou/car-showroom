from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Car, Service, Transaction
from .forms import CarForm, ServiceForm, TransactionForm

def index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars:index')
    else:
        form = CarForm()

    return render(request, 'cars/create.html', {'form': form})

def detail_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    services = car.services.all()
    return render(request, 'cars/detail.html', {'car': car, 'services': services})

def create_car_service(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.car = car
            service.save()
            return redirect('car_detail', car_id=car.id)
    else:
        form = ServiceForm()

    return render(request, 'services/create.html', {'form': form, 'car': car})

def service_index(request):
    services = Service.objects.all()
    return render(request, 'services/index.html', {'services': services})

def transaction_index(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/index.html', {'transactions': transactions})

def create_car_transaction(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        if 'confirm_transaction' in request.POST:
            # Handle the final confirmation
            form_data = request.POST
            transaction = Transaction.objects.create(
                car=car,
                is_loan=form_data['is_loan'] == 'on',
                annual_interest_rate=form_data['annual_interest_rate'],
                total_cost=form_data['total_cost']
            )

            # Mark the car as sold
            car.is_sold = True
            car.save()

            # Redirect to the success page after the transaction is saved
            return redirect('cars:transaction_index')

        else:
            # If coming from the initial form, go to the confirmation page
            form = TransactionForm(request.POST)
            if form.is_valid():
                form_data = form.cleaned_data
                return render(request, 'transactions/confirmation.html', {
                    'form_data': form_data,
                    'car': car
                })
    else:
        # Handle GET request to show the form page
        form = TransactionForm()
        return render(request, 'transactions/create.html', {'form': form, 'car': car})