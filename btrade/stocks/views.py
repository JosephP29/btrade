from django.shortcuts import render, redirect
from stocks.models import Stock, User_Stock, BuyReceipt, SellReceipt, HistoryStock
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
                if (user_s.units >= sell_form.units):
                    user_s.units -= sell_form.units
                    print(user_s.units)
                    if (user_s.units == 0):
                        print("*****DELETE User_Stock*****")
                    u.currency += s.price * sell_form.units
                    u.earned_currency += s.price * sell_form.units
                    user_s.save()
                    u.save()
                    sell_form.save()
                    return redirect('/account/profile')
                else:
                    print("*****SELLING MORE THAN YOU OWN*****")
                    sell_form = SellStockForm()
                    args = {'form': sell_form, 'stock': s}
                    return render(request, 'stocks/sellstock.html', args)

            except User_Stock.DoesNotExist:
                print("*****NO USER STOCK MODEL*****")
                sell_form = SellStockForm()
                args = {'form': buy_form, 'stock': s}
                return render(request, 'stocks/sellstock.html', args)
        else:
            print("*****FORM NOT VALID*****")
            sell_form = SellStockForm()
            args = {'form': sell_form, 'stock': s}
            return render(request, 'stocks/sellstock.html', args)
    else:
        sell_form = SellStockForm()
        args = {'form': sell_form, 'stock': s}
        return render(request, 'stocks/sellstock.html', args)

def stockdetail(request, curr_type):
    s1 = Stock.objects.get(curr_type=curr_type)
    user_stock = User_Stock.objects.get(owner=request.user, stock_curr_type=curr_type)

    l1 = HistoryStock.objects.filter(curr_type=s1.curr_type).order_by('date_entered').values_list('price', flat=True)
    list1 = list(l1)
    l2 = HistoryStock.objects.filter(curr_type=s1.curr_type).order_by('date_entered').values_list('date_entered', flat=True)

    dates = []
    for date in l2:
        dates.append(date.strftime("%b %d, %Y %I:%M %p"))

    list1.append(s1.price)
    dates.append(s1.date_entered.strftime("%b %d, %Y %I:%M %p"))

    s = {'stock': Stock.objects.get(curr_type=curr_type), 'prices': list1, 'dates': dates, 'ustock': user_stock }
	#stockid = request.GET['stockid']
    return render(request, 'stocks/stockdetail.html', s)

def savestock(request, pk):
    stock = Stock.objects.get(pk=pk)
    user_stock = User_Stock.objects.get(owner=request.user, stock_curr_type=stock.curr_type)
    user_stock.saved = not user_stock.saved
    user_stock.save()
    return redirect('/account/')
