from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Car, Service
from .forms import CarForm, ServiceForm

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