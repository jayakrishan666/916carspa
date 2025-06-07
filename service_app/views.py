from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Customer, ServicePart
from django.contrib import messages

# Create your views here.

def main_menu(request):
    return render(request, 'service_app/main_menu.html')

def service_form(request):
    return render(request, 'service_app/base.html')

def service_list(request):
    customers = Customer.objects.all().order_by('-created_at')
    return render(request, 'service_app/service_list.html', {'customers': customers})

def view_bill(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    total_amount = sum(float(part.total_price) for part in customer.service_parts.all())
    return render(request, 'service_app/bill.html', {
        'customer': customer,
        'total_amount': total_amount
    })

def print_bill(request, customer_id):
    return view_bill(request, customer_id)

def create_service(request):
    if request.method == 'POST':
        try:
            # Create customer
            customer = Customer.objects.create(
                name=request.POST.get('customer_name'),
                phone_number=request.POST.get('phone_number', ''),
                vehicle_number=request.POST.get('vehicle_number'),
                vehicle_model=request.POST.get('vehicle_model', '')
            )
            
            # Create service parts
            i = 0
            while f'part_name_{i}' in request.POST:
                part_name = request.POST.get(f'part_name_{i}')
                quantity = request.POST.get(f'quantity_{i}')
                price = request.POST.get(f'price_{i}')
                
                ServicePart.objects.create(
                    customer=customer,
                    part_name=part_name,
                    quantity=quantity,
                    price=price
                )
                i += 1
            
            return redirect('service_list')
            
        except Exception as e:
            return render(request, 'service_app/create_service.html', {
                'error': str(e)
            })
    
    # GET request: Show the create service form
    return render(request, 'service_app/create_service.html')

@require_http_methods(["GET"])
def get_service(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        parts = customer.service_parts.all()
        
        response_data = {
            'customer': {
                'name': customer.name,
                'phone_number': customer.phone_number,
                'vehicle_number': customer.vehicle_number,
                'vehicle_model': customer.vehicle_model
            },
            'parts': [
                {
                    'part_name': part.part_name,
                    'quantity': part.quantity,
                    'price': float(part.price),
                    'total_price': float(part.total_price)
                }
                for part in parts
            ],
            'total_amount': sum(float(part.total_price) for part in parts)
        }
        
        return JsonResponse(response_data)
        
    except Customer.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Customer not found'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def edit_service(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        try:
            # Get data from form
            customer_data = json.loads(request.POST.get('customer', '{}'))
            parts_data = json.loads(request.POST.get('parts', '[]'))
            
            # Update customer
            customer.name = customer_data.get('name', customer.name)
            customer.phone_number = customer_data.get('phone_number', customer.phone_number)
            customer.vehicle_number = customer_data.get('vehicle_number', customer.vehicle_number)
            customer.vehicle_model = customer_data.get('vehicle_model', customer.vehicle_model)
            customer.save()
            
            # Update or create service parts
            # Remove existing parts that are not in the new data
            new_part_ids = [part.get('id') for part in parts_data if part.get('id')]
            customer.service_parts.exclude(id__in=new_part_ids).delete()

            total_amount = 0
            for part_data in parts_data:
                part_id = part_data.get('id')
                if part_id:
                    # Update existing part
                    part = ServicePart.objects.get(id=part_id, customer=customer)
                    part.part_name = part_data.get('part_name', part.part_name)
                    part.quantity = part_data.get('quantity', part.quantity)
                    part.price = part_data.get('price', part.price)
                    part.save()
                else:
                    # Create new part
                    part = ServicePart.objects.create(
                        customer=customer,
                        part_name=part_data.get('part_name'),
                        quantity=part_data.get('quantity', 1),
                        price=part_data.get('price', 0)
                    )
                total_amount += part.total_price
            
            return JsonResponse({
                'status': 'success',
                'customer_id': customer.id,
                'total_amount': total_amount
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)

    else:
        # GET request: Render the edit form
        parts_list = [
            {
                'id': part.id,
                'part_name': part.part_name,
                'quantity': part.quantity,
                'price': float(part.price)
            }
            for part in customer.service_parts.all()
        ]
        total_amount = sum(float(part.total_price) for part in customer.service_parts.all())

        context = {
            'customer': {
                'id': customer.id,
                'name': customer.name,
                'phone_number': customer.phone_number,
                'vehicle_number': customer.vehicle_number,
                'vehicle_model': customer.vehicle_model
            },
            'parts': parts_list,
            'total_amount': total_amount
        }
        return render(request, 'service_app/edit_bill.html', context)

@require_http_methods(["POST"])
def delete_bill(request, customer_id):
    try:
        customer = get_object_or_404(Customer, id=customer_id)
        customer.delete()  # This will also delete related service parts due to CASCADE
        return redirect('service_list')
    except Exception as e:
        messages.error(request, f'Error deleting service bill: {str(e)}')
        return redirect('service_list')
