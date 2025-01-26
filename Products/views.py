from django.shortcuts import render
from .models import Category, Product
from .serializers import CategorySerializer
from .permissions import CustomPermission
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache

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


class CategoryAPIView(APIView):
    def get(self, request):
        if cache.get('categories'):
            categories = cache.get('categories')
            print('Cache hit')
            return Response(categories, status=status.HTTP_200_OK)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        cache.set('categories', serializer.data, timeout=60)
        print('Cache miss')
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CategoryDetailAPIView(APIView):
    def get(self, request, id):
        if Category.objects.filter(id=id).exists():
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        if Category.objects.filter(id=id).exists():
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, id):
        if Category.objects.filter(id=id).exists():
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        if Category.objects.filter(id=id).exists():
            category = Category.objects.get(id=id)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermission]
    
    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().list(request, *args, **kwargs)
        return Response({ "detail": "Authentication credentials were not provided."}, 
                        status=status.HTTP_401_UNAUTHORIZED)
    
    
# API authorization classificaiton
# 1. No authorization -> Public API -> Anonymous user can access
# 2. Token based authorization -> Private API -> Only authenticated users can access
# 3. Authorization based on roles -> Role based API -> Only users with specific roles can access
    
