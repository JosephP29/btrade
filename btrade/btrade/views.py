from django.shortcuts import render, redirect

def login_redirect(request):
    return redirect('/account/login')

def index(request):
    return render(request, 'main/index.html')
