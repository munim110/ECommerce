from django.shortcuts import render, redirect
from Users.models import Customer
from Home.views import home
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)          
        return render(request, 'login.html')
    return render(request, 'login.html')