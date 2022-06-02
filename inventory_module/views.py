from django.shortcuts import render, redirect

from .models import *
from .forms import CreateCustomerForm, OrderForm, UpdateCustomerForm 
# Create your views here.

def inventory_home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all() 
    total_customer = customers.count()
    total_orders= orders.count()  
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()
    out_for_del = orders.filter(status='Out For Delivery'). count()
    context = {
        'all_orders':orders, 
        'all_customers':customers,
        'total_customer':total_customer,
        'total_orders':total_orders,
        'pending':pending,
        'delivered':delivered,
        'out_for_del':out_for_del,

    }
    return render(request, 'inventory/dashboard.html', context)


def products(request):
    products = Stock.objects.all()
    context ={
        'all_products':products
    }
    return render(request, 'inventory/products.html', context)






def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()  #here fetch specific customer's order information. 
    total_orders = orders.count()
    context = {
        'customer':customer,
        'orders':orders,
        'total_orders': total_orders,
    }
    return render(request, 'inventory/customer.html', context)


def create_customer(request):
    form = CreateCustomerForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory-home-page')
    context ={
        'form':form,
    }
    return render(request, 'inventory/create_customer.html', context)


def update_customer(request, id):
    update_customer = Customer.objects.get(pk=id)
    form = UpdateCustomerForm(instance=update_customer) 
    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST, instance=update_customer) 
        if form.is_valid():
            form.save() 
            return redirect('inventory-home-page')
    context ={
        'form':form,
    }
    return render(request, 'inventory/create_customer.html', context)

def create_order(request, pk):   
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('inventory-home-page')
    context ={'form':form,
        'customer':customer,
    }
    return render(request, 'inventory/order_form.html', context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order) 
        if form.is_valid():
            form.save() 
            return redirect('inventory-home-page')
    context = {'form':form}
    return render(request, 'inventory/order_form.html', context)    


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete() 
        return redirect('inventory-home-page')
    context ={
        'item': order.product.name
    }

    return render(request, 'inventory/order_delete.html', context )