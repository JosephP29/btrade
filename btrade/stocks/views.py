from django.shortcuts import render
from stocks.models import Stock, User_Stock
from django.contrib.auth.models import User

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
	user_stock = User_Stock.objects.create(owner=request.user, units=1, price_bought_at=s.price, stock_curr_type=s.curr_type)
	u = request.user.userprofile
	if u.currency > s.price:
		u.currency -= s.price
		u.save()
	return render(request, 'stocks/confirmbuy.html')
	#insert buying stock failed