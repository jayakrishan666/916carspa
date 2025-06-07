from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('create-service/', views.create_service, name='create_service'),
    path('services/', views.service_list, name='service_list'),
    path('bill/<int:customer_id>/', views.view_bill, name='view_bill'),
    path('bill/<int:customer_id>/print/', views.print_bill, name='print_bill'),
    path('bill/<int:customer_id>/edit/', views.edit_service, name='edit_service'),
    path('bill/<int:customer_id>/delete/', views.delete_bill, name='delete_bill'),
    path('api/services/<int:customer_id>/', views.get_service, name='get_service'),
] 