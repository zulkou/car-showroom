from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_car, name='create'),
    path('<uuid:car_id>/', views.detail_car, name='detail'),
]
