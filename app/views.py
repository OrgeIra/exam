from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'chackout.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

def shop_detail(request):
    return render(request, 'shop-detail.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def error_404(request, exception):
    return render(request, '404.html')