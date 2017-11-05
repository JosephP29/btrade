from django.shortcuts import render, redirect

def login_redirect(request):
    return redirect('/account/login')

def index(request):
    return render(request, 'main/index.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def info(request):
    return render(request, 'accounts/info.html')

def portfolio(request):
    return render(request, 'accounts/portfolio.html')

def edit(request):
    return render(request, 'accounts/edit_profile.html')

def admin(request):
    return render(request, 'admin/admin_search.html')

