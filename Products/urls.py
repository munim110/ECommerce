from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('products', all_products, name='products'),
    path('product/<int:id>', product_detail, name='product_detail'),
    path('api/categories/<int:id>/', CategoryDetailAPIView.as_view(), name='api_categories'),
    path('api/categories/', CategoryAPIView.as_view(), name='api_categories'),
] + router.urls
