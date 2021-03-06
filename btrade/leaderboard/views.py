from operator import itemgetter
from collections import OrderedDict
from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import UserProfile
from stocks.models import BuyReceipt, SellReceipt, SavedStock, current_price_table
from decimal import Decimal


# Create your views here.
def home(request):
    users = User.objects.all()
    price_table = current_price_table.objects.all()

    total_holdings = {}
    for user in users:
        total_holdings[user] = 0
        user_coin_list = user.user_stock_set.all()
        for coin in user_coin_list:
            current_entry = current_price_table.objects.get(coin_type=coin.coin_type)
            current_price = current_entry.price
            units = coin.units
            total_coin_value = current_price * units
            total_holdings[user] += total_coin_value
        account_balance = user.userprofile.currency
        total_holdings[user] += account_balance

    sorted_users = OrderedDict(sorted(total_holdings.items(), key=itemgetter(1), reverse=True))
    for user in sorted_users:
        sorted_users[user] = '%.2f' % sorted_users[user]
    return render(request, 'leaderboard/home.html', {'users': sorted_users, 'total_holdings': total_holdings})
