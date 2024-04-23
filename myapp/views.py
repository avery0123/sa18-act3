from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})

def show(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'myapp/show.html', {'product': product})
