
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache
# Create your views here.



@never_cache
def login_user(request):
    print("In logn 8888888888")
    if 'username' in request.session:
        return redirect(home)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        
        if user is not None:
            request.session['username'] = username
            return redirect(home)
        else:
            print("Invalid credentials")
    return render(request, 'login.html')

@never_cache
def home(request):
    if 'username' in request.session:
        return render(request, 'home.html')
    return redirect(login_user)

@never_cache
def user_logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(login_user)



   
