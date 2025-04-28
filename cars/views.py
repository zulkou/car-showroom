from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Car
from .forms import CarForm

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
    return render(request, 'cars/detail.html', {'car': car})