from django.urls import path
from .views import *

urlpatterns = [
    path('products', all_products, name='products'),
    path('product/<int:id>', product_detail, name='product_detail'),
]
