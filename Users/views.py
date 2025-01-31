from django.shortcuts import render, redirect, reverse
from .models import Customer
from Chat.views import chat
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password

# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Customer.objects.get(username=username)
        except:
            context = {
                "message": "User not found. Please sign up."
            }
            return render(request, 'login.html', context)
        if check_password(password, user.password):
            login(request, user)
            return redirect(reverse('channel_list'))
        context = {
            "message": "Invalid password. Please try again."
        }
        return render(request, 'login.html', context)
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        if password == password2:
            user = Customer.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            user.save()
            return redirect(signin)
    return render(request, 'signup.html')