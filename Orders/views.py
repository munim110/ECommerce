from django.shortcuts import render, redirect
from .models import Cart

# Create your views here.

def CartView(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    user = request.user
    cart = Cart.objects.filter(user=user).first()
    if not cart:
        cart = Cart.objects.create(user=user)
    cart_items = Cart.products.through.objects.filter(cart=cart)
    return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items})