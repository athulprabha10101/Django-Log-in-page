
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
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
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect(login_user)

@never_cache
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(login_user)



   
