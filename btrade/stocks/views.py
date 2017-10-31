from django.shortcuts import render
from stocks.models import Stock, User_Stock, BuyReceipt, SellReceipt
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.
def stocks(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/stocks.html', {'stocks': stocks})

def stockdetail(request, pk):
	s = {'stock': Stock.objects.get(pk=pk)}
	#stockid = request.GET['stockid']
	return render(request, 'stocks/stockdetail.html', s)

def confirmbuy(request, pk):
    s = Stock.objects.get(pk=pk)
	#qs = request.user.user_stock_set.all()
    try:
	    use_s = request.user.user_stock_set.get(stock_curr_type=s.curr_type)
		#use_s.update(price_bought_at=F('price_bought_at') + s.price, units=F('units') + 5, date_bought=datetime.now())
	    use_s.price_bought_at += s.price
	    use_s.units += 5
	    use_s.date_bought = datetime.now()
	    use_s.save(update_fields=['price_bought_at', 'units', 'date_bought'])
    except User_Stock.DoesNotExist:
        user_stock = User_Stock.objects.create(owner=request.user, units=1, price_bought_at=s.price, stock_curr_type=s.curr_type)
    u = request.user.userprofile
    if u.currency > s.price:
        buy_receipt = BuyReceipt.objects.create(owner=request.user, units=1, price_bought_at=s.price, curr_type=s.curr_type)
        u.currency -= s.price
		#u.update(currency=F('currency') - s.price)
        u.save(update_fields=['currency'])
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
