from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                user = User.objects.create_user(username = username, password = password)
                user.save()
                login(request, user)
                return redirect('home')
            except:
                messages.error(request, "Username Already Exists")
        else:
            messages.error(request, "Password don't match")
    return render(request, "registration/registration.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username or password')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect(request, 'login')