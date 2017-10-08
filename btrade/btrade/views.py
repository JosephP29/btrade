from django.shortcuts import render, redirect

def login_redirect(request):
    return redirect('/account/login')

def index(request):
    return render(request, 'main/index.html')

def login(request):
    return render(request, 'accounts/login.html')

def signUp(request):
    return render(request, 'accounts/signUp.html')
