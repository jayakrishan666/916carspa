from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    vehicle_number = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.vehicle_number}"

class ServicePart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='service_parts')
    part_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.part_name} - {self.customer.name}"

    @property
    def total_price(self):
        return self.quantity * self.price
