from django.shortcuts import render, redirect
from stocks.models import (
    Stock,
    User_Stock,
    BuyReceipt,
    SellReceipt,
    HistoryStock,
    SavedStock,
    current_price_table,
    history,
)
from django.contrib.auth.models import User
from datetime import datetime
from stocks.forms import BuyStockForm, SellStockForm
from django import forms

# Create your views here.
def stocks(request):
    sorted_price_table = current_price_table.objects.all().order_by('-mktcap')
    return render(request, 'stocks/stocks.html', {'price_table': sorted_price_table})

def trending(request):
    sorted_price_table = current_price_table.objects.all().order_by('-change24hour')
    return render(request, 'stocks/trending.html', {'trending_table': sorted_price_table})


def buystock(request, coin_type):
    coin = current_price_table.objects.get(coin_type=coin_type)
    u = request.user.userprofile
    if request.method == 'POST':
        buy_form = BuyStockForm(request.POST)
        if buy_form.is_valid():
            buy_form = buy_form.save(commit=False)
            buy_form.owner = request.user
            buy_form.coin_type = coin.coin_type
            buy_form.price_bought_at = coin.price
            buy_form.buy_total = coin.price * buy_form.units

            if (u.currency >= buy_form.units * coin.price):
                try:
                    user_s = User_Stock.objects.get(owner=request.user, coin_type=coin_type)
                    user_s.units += buy_form.units
                    u.currency -= coin.price * buy_form.units
                    user_s.netgain -= (coin.price * buy_form.units)
                    user_s.save()
                except User_Stock.DoesNotExist:
                    User_Stock.objects.create(owner=request.user, units=buy_form.units, coin_type=coin_type, netgain=(coin.price*buy_form.units*-1))
                    u.currency -= coin.price * buy_form.units

                u.save()
                buy_form.save()
                return redirect('/account/profile')
            else:
                buy_form = BuyStockForm()
                args = {'form': buy_form, 'coin': coin}
                print("***** NOT ENOUGH MONEY *****")
                return render(request, 'stocks/buystock.html', args)
    else:
        buy_form = BuyStockForm()
        args = {'form': buy_form, 'coin_type': coin_type, 'coin': coin}
        return render(request, 'stocks/buystock.html', args)

def sellstock(request, coin_type):
    coin = current_price_table.objects.get(coin_type=coin_type)
    u = request.user.userprofile
    if request.method == 'POST':
        sell_form = SellStockForm(request.POST)
        if sell_form.is_valid():
            sell_form = sell_form.save(commit=False)
            sell_form.owner = request.user
            sell_form.coin_type = coin.coin_type
            sell_form.price_sold_at = coin.price
            sell_form.sell_total = coin.price * sell_form.units

            try:
                user_s = User_Stock.objects.get(owner=request.user, coin_type=coin_type)
                if (user_s.units >= sell_form.units):
                    user_s.units -= sell_form.units
                    user_s.netgain += (coin.price * sell_form.units)
                    u.currency += coin.price * sell_form.units
                    u.earned_currency += coin.price * sell_form.units

                    if (user_s.units == 0):
                        user_s.delete()
                    else:
                        user_s.save()
                    u.save()
                    sell_form.save()
                    return redirect('/account/profile')
                else:
                    print("*****SELLING MORE THAN YOU OWN*****")
                    sell_form = SellStockForm()
                    args = {'form': sell_form, 'coin': coin}
                    return render(request, 'stocks/sellstock.html', args)

            except User_Stock.DoesNotExist:
                print("*****NO USER STOCK MODEL*****")
                sell_form = SellStockForm()
                args = {'form': buy_form, 'coin': coin}
                return render(request, 'stocks/sellstock.html', args)
        else:
            print("*****FORM NOT VALID*****")
            sell_form = SellStockForm()
            args = {'form': sell_form, 'coin': coin}
            return render(request, 'stocks/sellstock.html', args)
    else:
        sell_form = SellStockForm()
        args = {'form': sell_form, 'coin_type': coin_type, 'coin': coin}
        return render(request, 'stocks/sellstock.html', args)

def stockdetail(request, coin_type):
    #s1 = history.objects.get(coin_type=coin_type)
    user = request.user
    sorted_history_table = history.objects.filter(coin_type=coin_type).order_by('-time')[:10]
    try:
        saved = SavedStock.objects.get(owner=user, coin_type=coin_type)
        args = { 'history_table': sorted_history_table,
                 'coin_type': coin_type,
                 'savedstock': saved, }
    except:
        args = { 'history_table': sorted_history_table, 'coin_type': coin_type, }

    return render(request, 'stocks/stockdetail.html', args)



def savestock(request, coin_type):
    user = request.user
    stock = current_price_table.objects.get(coin_type=coin_type)
    save_stock = SavedStock.objects.create(owner=request.user, coin_type=stock.coin_type)
    save_stock.save()
    return redirect('/account/')

def unsavestock(request, coin_type):
    user = request.user
    stock = Stock.objects.get(coin_type=coin_type)
    save_stock = SavedStock.objects.filter(owner=user, coin_type=stock.coin_type).delete()
    return redirect('/account/')
