from django.contrib import admin
from stocks.models import Stock, User_Stock, BuyReceipt, SellReceipt, HistoryStock

# Register your models here.
admin.site.register(Stock)

admin.site.register(User_Stock)

admin.site.register(BuyReceipt)

admin.site.register(SellReceipt)

admin.site.register(HistoryStock)
