from django.contrib import admin
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

# Register your models here.
admin.site.register(Stock)

admin.site.register(User_Stock)

admin.site.register(BuyReceipt)

admin.site.register(SellReceipt)

admin.site.register(HistoryStock)

admin.site.register(SavedStock)

admin.site.register(current_price_table)

admin.site.register(history)
