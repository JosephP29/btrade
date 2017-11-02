from django.shortcuts import render, redirect
from stocks.models import Stock, User_Stock, BuyReceipt, SellReceipt
from django.contrib.auth.models import User
from datetime import datetime
from stocks.forms import BuyStockForm, SellStockForm
from django import forms

# Create your views here.
def stocks(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/stocks.html', {'stocks': stocks})

# NOTE: LOTS OF TEST CASES HERE
def buystock(request, pk):
    s = Stock.objects.get(pk=pk)
    u = request.user.userprofile
    if request.method == 'POST':
        buy_form = BuyStockForm(request.POST)
        if buy_form.is_valid():
            buy_form = buy_form.save(commit=False)
            buy_form.owner = request.user
            buy_form.curr_type = s.curr_type
            buy_form.price_bought_at = s.price

            if (u.currency >= buy_form.units * s.price):
                try:
                    user_s = User_Stock.objects.get(owner=request.user, stock_curr_type=s.curr_type)
                    user_s.units += buy_form.units
                    u.currency -= s.price * buy_form.units
                    user_s.save()
                except User_Stock.DoesNotExist:
                    User_Stock.objects.create(owner=request.user, units=buy_form.units, stock_curr_type=s.curr_type)
                    u.currency -= s.price * buy_form.units

                u.save()
                buy_form.save()
                return redirect('/account/profile')
            else:
                buy_form = BuyStockForm()
                args = {'form': buy_form, 'stock': s}
                print("***** NOT ENOUGH MONEY *****")
                return render(request, 'stocks/buystock.html', args)
    else:
        buy_form = BuyStockForm()
        args = {'form': buy_form, 'stock': s}
        return render(request, 'stocks/buystock.html', args)

def sellstock(request, pk):
    s = Stock.objects.get(pk=pk)
    u = request.user.userprofile
    if request.method == 'POST':
        sell_form = SellStockForm(request.POST)
        if sell_form.is_valid():
            sell_form = sell_form.save(commit=False)
            sell_form.owner = request.user
            sell_form.curr_type = s.curr_type
            sell_form.price_sold_at = s.price

            try:
                user_s = User_Stock.objects.get(owner=request.user, stock_curr_type=s.curr_type)
                print(user_s)
                print(user_s.units)
                print(sell_form.units)
                if (user_s.units >= sell_form.units):
                    print("HELLO WORLD")
                    user_s.units -= sell_form.units
                    u.currency += s.price * sell_form.units
                    user_s.save()
                    u.save()
                    sell_form.save()
                    return redirect('/account/profile')
            except User_Stock.DoesNotExist:
                print("*****NO STOCKS*****")
                sell_form = SellStockForm()
                args = {'form': buy_form, 'stock': s}
                return render(request, 'stocks/sellstock.html', args)
        else:
            print("*****ERROR*****")
            sell_form = SellStockForm()
            args = {'form': buy_form, 'stock': s}
            return render(request, 'stocks/sellstock.html', args)
    else:
        sell_form = SellStockForm()
        args = {'form': sell_form, 'stock': s}
        return render(request, 'stocks/sellstock.html', args)

def stockdetail(request, pk):
	s = {'stock': Stock.objects.get(pk=pk)}
	#stockid = request.GET['stockid']
	return render(request, 'stocks/stockdetail.html', s)

# NOTE: Pretty much moved into buystock function
def confirmbuy(request, pk):
    # s = Stock.objects.get(pk=pk)
    # #qs = request.user.user_stock_set.all()
    # try:
    #     use_s = request.user.user_stock_set.get(stock_curr_type=s.curr_type)
    #     #use_s.update(price_bought_at=F('price_bought_at') + s.price, units=F('units') + 5, date_bought=datetime.now())
    #     use_s.price_bought_at += s.price
    #     use_s.units += 5
    #     use_s.date_bought = datetime.now()
    #     use_s.save(update_fields=['price_bought_at', 'units', 'date_bought'])
    # except User_Stock.DoesNotExist:
    #     user_stock = User_Stock.objects.create(owner=request.user, units=1, price_bought_at=s.price, stock_curr_type=s.curr_type)
    #     u = request.user.userprofile
    #     if u.currency > s.price:u.currency -= s.price
    #     #u.update(currency=F('currency') - s.price)
    #     u.save(update_fields=['currency'])
    return render(request, 'stocks/confirmbuy.html')
        #insert buying stock failed

def confirmsell(request, pk):
    st = Stock.objects.get(pk=pk)
    try:
        user_s = request.user.user_stock_set.get(stock_curr_type=st.curr_type)
        user_s.units -= 1
        user_s.date_sold = datetime.now()
	    #use_s.update(units=F('units')-1, date_bought=datetime.now())
	    #s.price_sold_at = s.price_bought_at  #change this crap later
        user_s.save(update_fields=['units', 'date_sold'])
        us = request.user.userprofile
        #u.update(currency=F('currency') + s.price)
        us.currency += user_s.price_bought_at
        sell_receipt = SellReceipt.objects.create(owner=request.user, units=1, price_sold_at=st.price, curr_type=st.curr_type)
        us.save(update_fields=['currency'])
    except User_Stock.DoesNotExist:
        #doesn't exist so we can't sell
        s1 = Stock.objects.get(pk=pk)
    return render(request, 'stocks/confirmsell.html')
	#insert buying stock failed
