from django.shortcuts import render
from stocks.models import Stock

# Create your views here.
def stocks(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/stocks.html', {'stocks': stocks})

def buystock(request):
    return render(request, 'stocks/buystock.html')
