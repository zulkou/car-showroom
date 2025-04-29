from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_car, name='create_car'),
    path('<uuid:car_id>/', views.detail_car, name='detail_car'),
    path('services/create/<uuid:car_id>', views.create_car_service, name='create_car_service'),
    path('transactions/create/<uuid:car_id>', views.create_car_transaction, name='create_car_transaction'),
    path('transaction/confirm/<uuid:car_id>', views.confirm_car_transaction, name='confirm_car_transaction'),
    path('delete/<uuid:car_id>/', views.delete_car, name='delete_car'),
]
