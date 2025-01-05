from django.shortcuts import render, redirect
from .models import Cart
from .serializers import CartProductSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

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


class AddtoCartView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        product_id = request.data.get('product_id')
        cart = Cart.objects.filter(user=user).first() # Cart.objects.get(user=user)
        if not cart:
            cart = Cart.objects.create(user=user)
        cart_product = cart.products.through.objects.filter(cart=cart, product_id=product_id).first()
        if cart_product:
            cart_product.quantity += 1
            cart_product.save()
        else:
            # Add new product to cart with quantity 1 and unit pcs
            cart.products.add(product_id)
            return Response({'message': 'Product added to cart'}, status=status.HTTP_201_CREATED)
        
        
class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        product_id = request.data.get('product_id')
        cart = Cart.objects.filter(user=user).first()
        if not cart:
            return Response({'message': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
        cart_product = cart.products.through.objects.filter(cart=cart, product_id=product_id).first()
        if cart_product:
            cart_product.quantity -= 1
            cart_product.save()
            if cart_product.quantity == 0:
                cart.products.remove(product_id)
            return Response({'message': 'Product removed from cart'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Product not in cart'}, status=status.HTTP_400_BAD_REQUEST)
        