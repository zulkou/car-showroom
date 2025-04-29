import uuid
import datetime
from django.db import models

# Car Model
class Car(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    base_price = models.BigIntegerField()
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
    
class Service(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="services")
    date = models.DateField(default=datetime.date.today)
    description = models.TextField()
    cost = models.BigIntegerField()
    
    def __str__(self):
        return f"{self.car} serviced in {self.created_at}"

class Transaction(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="transactions")
    is_loan = models.BooleanField()
    down_payment = models.BigIntegerField(null=True)
    tenor = models.IntegerField(null=True)
    annual_interest_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True)