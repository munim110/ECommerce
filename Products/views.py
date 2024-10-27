from django.shortcuts import render
from .models import *

# Create your views here.

def all_products(request):
    all_products = Product.objects.all()
    context = {
        "products": all_products
    }
    return render(request, 'all_products.html', context)

def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        product = None
    context = {
        "product": product
    }
    return render(request, 'product_details.html', context)