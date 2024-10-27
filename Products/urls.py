from django.urls import path
from .views import *

urlpatterns = [
    path('products', all_products, name='products'),
]
