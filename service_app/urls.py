from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('create/', views.service_form, name='service_form'),
    path('services/', views.service_list, name='service_list'),
    path('bill/<int:customer_id>/', views.view_bill, name='view_bill'),
    path('bill/<int:customer_id>/print/', views.print_bill, name='print_bill'),
    path('bill/<int:customer_id>/edit/', views.edit_service, name='edit_service'),
    path('api/services/', views.create_service, name='create_service'),
    path('api/services/<int:customer_id>/', views.get_service, name='get_service'),
] 