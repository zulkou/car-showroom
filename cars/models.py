import uuid
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

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
    
class Service(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid3,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="services")
    description = models.TextField()
    cost = models.BigIntegerField()
    
    def __str__(self):
        return f"{self.car} serviced in {self.created_at}"

class Payment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="payments")
    is_loan = models.BooleanField()
    annual_interest_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True)