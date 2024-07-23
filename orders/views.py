from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from products.models import Product

@login_required
def order_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        Order.objects.create(user=request.user, product=product, quantity=quantity)
        return redirect('order_list')
    return render(request, 'orders/order_create.html', {'product': product})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})
