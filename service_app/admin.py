from django.contrib import admin
from .models import Customer, ServicePart

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'vehicle_number', 'vehicle_model', 'created_at')
    search_fields = ('name', 'vehicle_number', 'phone_number')

@admin.register(ServicePart)
class ServicePartAdmin(admin.ModelAdmin):
    list_display = ('part_name', 'customer', 'quantity', 'price', 'total_price', 'created_at')
    list_filter = ('customer',)
    search_fields = ('part_name', 'customer__name')
