from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from stocks.models import BuyReceipt, SellReceipt, SavedStock, current_price_table

# Create your views here.
@login_required
def home(request):
    qs = request.user.user_stock_set.all()
    saved_stocks = SavedStock.objects.filter(owner=request.user)
    s1 = None#qs[0]
    s2 = None#qs[1]
    s3 = None#qs[2]

    if (saved_stocks.count() == 1):
        saved1 = saved_stocks[0]
        args = {'stock1': s1, 'stock2': s2, 'stock3': s3, 'saved1': saved1}
    elif (saved_stocks.count() == 2):
        saved1 = saved_stocks[0]
        saved2 = saved_stocks[1]
        args = {'stock1': s1, 'stock2': s2, 'stock3': s3, 'saved1': saved1, 'saved2': saved2}
    elif (saved_stocks.count() == 3):
        saved1 = saved_stocks[0]
        saved2 = saved_stocks[1]
        saved3 = saved_stocks[2]
        args = {'stock1': s1, 'stock2': s2, 'stock3': s3, 'saved1': saved1, 'saved2': saved2, 'saved3': saved3}
    else:
        args = {'stock1': s1, 'stock2': s2, 'stock3': s3}
    return render(request, 'accounts/home.html', args)

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

@login_required
def view_profile(request):
    coin_list = request.user.user_stock_set.all()
    current_prices = current_price_table.objects.all()
    buys = BuyReceipt.objects.filter(owner=request.user)
    price_differences = {}
    roi = {}

    for current_price in current_prices:
        for buy in buys:
            if current_price.coin_type == buy.coin_type:
                difference = current_price.price - buy.price_bought_at
                total = difference * buy.units
                roi[buy.coin_type] = str(round(total, 2))

    args = {'user': request.user,
            'coin_list': request.user.user_stock_set.all(),
            'current_prices': current_price_table.objects.all(),
            'buys': BuyReceipt.objects.filter(owner=request.user),
            'sales': SellReceipt.objects.filter(owner=request.user),
            'roi': roi,
        }
    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

# not currently using, will be used in future
def custom_login(request):
    if request.user.is_authenticated():
        return redirect('/account/')
    else:
        return render(request, 'main/index.html')
