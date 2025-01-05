from django.urls import path
from .views import *

urlpatterns = [
    path('cart', CartView, name='cart'),
    path('add-to-cart/', AddtoCartView.as_view(), name='add-to-cart'),
    path('remove-from-cart/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]