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
    hot_price_table = current_price_table.objects.all().order_by('-change24hour')
    args = { 'price_table': sorted_price_table, 'hot_table': hot_price_table, }
    return render(request, 'stocks/stocks.html', args)

def trending(request):
    sorted_price_table = current_price_table.objects.all().order_by('-change24hour')
    hot_price_table = current_price_table.objects.all().order_by('-change24hour')
    args = { 'trending_table': sorted_price_table, 'hot_table': hot_price_table, }
    return render(request, 'stocks/trending.html', args)


def buystock(request, coin_type):
    coin = current_price_table.objects.get(coin_type=coin_type)
    u = request.user.userprofile
    account_balance = u.currency
    print(account_balance)
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
                args = {'form': buy_form, 'coin': coin, 'account_balance': account_balance,}
                print("***** NOT ENOUGH MONEY *****")
                return render(request, 'stocks/buystock.html', args)
    else:
        buy_form = BuyStockForm()
        args = {'form': buy_form, 'coin': coin, 'account_balance': account_balance,}
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
                    args = {'form': sell_form, 'coin': coin, 'units': user_s.units}
                    return render(request, 'stocks/sellstock.html', args)

            except User_Stock.DoesNotExist:
                print("*****NO USER STOCK MODEL*****")
                sell_form = SellStockForm()
                args = {'form': buy_form, 'coin': coin,  'units': 0}
                return render(request, 'stocks/sellstock.html', args)
        else:
            print("*****FORM NOT VALID*****")
            sell_form = SellStockForm()
            try:
                user_s = User_Stock.objects.get(owner=request.user, coin_type=coin_type)
                units = user_s.units
            except User_Stock.DoesNotExist:
                units = 0
            args = {'form': sell_form, 'coin': coin, 'units': units}
            return render(request, 'stocks/sellstock.html', args)
    else:
        try:
            sell_form = SellStockForm()
            user_s = User_Stock.objects.get(owner=request.user, coin_type=coin_type)
            args = {'form': sell_form, 'coin_type': coin_type, 'coin': coin, 'units': user_s.units}
        except User_Stock.DoesNotExist:
            sell_form = SellStockForm()
            args = {'form': sell_form, 'coin_type': coin_type, 'coin': coin, 'units': 0}
        return render(request, 'stocks/sellstock.html', args)


def stockdetail(request, coin_type):
    user = request.user
    current_price = history.objects.filter(coin_type=coin_type).order_by('-time')[:1]
    price_15_minutes = history.objects.filter(coin_type=coin_type).order_by('-time')[14:15]
    price_30_minutes = history.objects.filter(coin_type=coin_type).order_by('-time')[29:30]
    price_60_minutes = history.objects.filter(coin_type=coin_type).order_by('-time')[60:61]
    price_6_hours = history.objects.filter(coin_type=coin_type).order_by('-time')[360:361]
    price_12_hours = history.objects.filter(coin_type=coin_type).order_by('-time')[720:721]
    price_24_hours = history.objects.filter(coin_type=coin_type).order_by('-time')[1439:1440]
    try:
        user_s = User_Stock.objects.get(owner=request.user, coin_type=coin_type)
        units = user_s.units
    except:
        units = 0
    try:
        saved = SavedStock.objects.get(owner=user, coin_type=coin_type)
        args = { 'current_price': current_price,
                 'price_15_minutes': price_15_minutes,
                 'price_30_minutes': price_30_minutes,
                 'price_60_minutes': price_60_minutes,
                 'price_6_hours': price_6_hours,
                 'price_12_hours': price_12_hours,
                 'price_24_hours': price_24_hours,
                 'coin_type': coin_type,
                 'units': units,
                 'savedstock': saved, }
    except:
        args = { 'current_price': current_price,
                 'price_15_minutes': price_15_minutes,
                 'price_30_minutes': price_30_minutes,
                 'price_60_minutes': price_60_minutes,
                 'price_6_hours': price_6_hours,
                 'price_12_hours': price_12_hours,
                 'price_24_hours': price_24_hours,
                 'coin_type': coin_type,
                 'units': units, }

    return render(request, 'stocks/stockdetail.html', args)


def savestock(request, coin_type):
    user = request.user
    stock = current_price_table.objects.get(coin_type=coin_type)
    save_stock = SavedStock.objects.create(owner=request.user, coin_type=stock.coin_type)
    save_stock.save()
    return redirect('/account/')

def unsavestock(request, coin_type):
    user = request.user
    coin = current_price_table.objects.get(coin_type=coin_type)
    save_stock = SavedStock.objects.filter(owner=user, coin_type=coin.coin_type).delete()
    return redirect('/account/')
