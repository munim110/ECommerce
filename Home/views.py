from django.shortcuts import render
from .models import KeyValuePair

# Create your views here.

def home(request):
    print(request.user)
    return render(request, 'home.html')
