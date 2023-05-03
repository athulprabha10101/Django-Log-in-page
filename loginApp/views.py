
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.



@never_cache
def login_user(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            print("Invalid credentials")
    return render(request, 'login.html')
@never_cache
@login_required(login_url='login/')
def home(request):
        return render(request, 'home.html')


@login_required(login_url='login/')
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(login_user)



   
