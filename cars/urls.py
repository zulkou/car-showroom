from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_car, name='create_car'),
    path('<uuid:car_id>/', views.detail_car, name='detail_car'),
    path('services/', views.service_index, name='service_index'),
    path('services/create/<uuid:car_id>', views.create_car_service, name='create_car_service'),
    path('transactions/', views.transaction_index, name='transcation_index'),
    path('transactions/create/<uuid:car_id>', views.create_car_transaction, name='create_car_transaction')
]
