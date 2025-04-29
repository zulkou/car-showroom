from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Service, Transaction
from .forms import CarForm, ServiceForm, TransactionForm
from .utils import calculate_loan_details
from decimal import Decimal

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
    transactions = car.transactions.all()
    transactions_detail = []

    for transaction in transactions:
        services_cost, loan_amount, monthly_payment, total_cost = calculate_loan_details(transaction, car)

        transactions_detail.append({
            'is_loan': transaction.is_loan,
            'down_payment': transaction.down_payment,
            'tenor': transaction.tenor,
            'annual_interest_rate': transaction.annual_interest_rate,
            'loan_amount': loan_amount,
            'services_cost': services_cost,
            'monthly_payment': monthly_payment,
            'total_cost': total_cost,
        })

    return render(request, 'cars/detail.html', {'car': car, 'services': services, 'transactions_detail': transactions_detail})

def create_car_service(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.car = car
            service.save()
            return redirect('cars:detail_car', car_id=car.id)
    else:
        form = ServiceForm()

    return render(request, 'services/create.html', {'form': form, 'car': car})

def create_car_transaction(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # Convert Decimals to strings for session storage
            session_data = {
                k: str(v) if isinstance(v, Decimal) else v
                for k, v in form.cleaned_data.items()
            }
            request.session['transaction_data'] = session_data
            return redirect('cars:confirm_car_transaction', car_id=car_id)
    
    else:
        form = TransactionForm()

    return render(request, 'transactions/create.html', {'form': form, 'car': car})


def confirm_car_transaction(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    session_data = request.session.get('transaction_data')

    # Redirect if no session data
    if not session_data:
        return redirect('cars:create_car_transaction', car_id=car_id)

    # Convert strings back to Decimals
    transaction_data = {
        k: Decimal(v) if isinstance(v, str) and '.' in v else v
        for k, v in session_data.items()
    }

    # Create unsaved transaction instance for calculations
    temp_transaction = Transaction(
        car=car,
        **transaction_data
    )
    
    # Calculate here instead of creation view
    services_cost, loan_amount, monthly_payment, total_cost = calculate_loan_details(temp_transaction, car)

    if request.method == 'POST':
        if 'confirm_transaction' in request.POST:
            # Create actual transaction
            Transaction.objects.create(car=car, **transaction_data)
            del request.session['transaction_data']
            return redirect('cars:detail_car', car_id=car_id)
        
        if 'cancel_transaction' in request.POST:
            del request.session['transaction_data']
            return redirect('cars:detail_car', car_id=car_id)

    return render(request, 'transactions/confirmation.html', {
        'context': {
            'car': car,
            **transaction_data,
            'services_cost': services_cost,
            'loan_amount': loan_amount,
            'monthly_payment': monthly_payment,
            'total_cost': total_cost
        }
    })