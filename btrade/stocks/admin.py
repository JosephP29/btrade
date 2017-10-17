from django.contrib import admin
from stocks.models import Stock, User_Stock

# Register your models here.
admin.site.register(Stock)

admin.site.register(User_Stock)
