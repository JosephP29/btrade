from django.shortcuts import render, redirect

def login_redirect(request):
    return redirect('/account/login')

def index(request):
    return render(request, 'main/index.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def logout(request):
    return render(request, 'accounts/logout.html')

