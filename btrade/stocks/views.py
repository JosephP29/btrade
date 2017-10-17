from django.shortcuts import render
from stocks.models import Stock, User_Stock
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.
def stocks(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/stocks.html', {'stocks': stocks})

def buystock(request, pk):
	s = {'stock': Stock.objects.get(pk=pk)}
	#stockid = request.GET['stockid']
	return render(request, 'stocks/buystock.html', s)

def confirmbuy(request, pk): 
	s = Stock.objects.get(pk=pk)
	user_stock = User_Stock.objects.create(owner=request.user, units=1, price_bought_at=s.price, stock_curr_type=s.curr_type)
	u = request.user.userprofile
	if u.currency > s.price:
		u.currency -= s.price
		u.save()
	return render(request, 'stocks/confirmbuy.html')
	#insert buying stock failed

def confirmsell(request, pk): 
	s = User_Stock.objects.get(pk=pk)
	s.sold = True
	s.date_sold = datetime.now()
	s.price_sold_at = s.price_bought_at  #change this crap later
	s.save()
	u = request.user.userprofile
	u.currency += s.price_bought_at
	u.save()
	return render(request, 'stocks/confirmsell.html')
	#insert buying stock failed	