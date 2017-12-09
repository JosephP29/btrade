from django.db import models
from django.utils import timezone
from btrade import settings
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    price = models.DecimalField(max_digits=13, decimal_places=2)
    coin_type = models.CharField(max_length=10, unique=True)
    date_entered = models.DateTimeField()

    # Gives clear name in admin page
    def __str__(self):
        return self.coin_type


class current_price_table(models.Model):
    time = models.DateTimeField('%Y-%m-%d %H:%M:%S')
    coin_type = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    volume = models.DecimalField(max_digits=20, decimal_places=2)
    mktcap = models.DecimalField(max_digits=20, decimal_places=2)


    # Gives clear name in admin page
    def __str__(self):
        return self.coin_type


class history(models.Model):
    time = models.DateTimeField('%Y-%m-%d %H:%M:%S')
    coin_type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    volume = models.DecimalField(max_digits=20, decimal_places=2)
    mktcap = models.DecimalField(max_digits=20, decimal_places=2)

    # Gives clear name in admin page
    def __str__(self):
        return self.coin_type

class User_Stock(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    units = models.DecimalField(max_digits=18, decimal_places=8)
    coin_type = models.CharField(max_length=10)
    date_bought = models.DateTimeField(auto_now=True)
    netgain = models.DecimalField(default=0.00, max_digits=10, decimal_places=3)

    # Gives clear name in admin page
    def __str__(self):
        string = str(self.owner) + " " + self.coin_type
        return string

class BuyReceipt(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    units = units = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    price_bought_at = models.DecimalField(max_digits=13, decimal_places=2)
    buy_total = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    coin_type = models.CharField(max_length=10)
    date_bought = models.DateTimeField(auto_now=True)

    # Give's clear name in admin page
    def __str__(self):
        string = str(self.owner) + " " + self.coin_type
        return string

class SellReceipt(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    units = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    #units = models.FloatField(default=0)
    price_sold_at = models.DecimalField(max_digits=13, decimal_places=2)
    sell_total = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    coin_type = models.CharField(max_length=10)
    date_bought = models.DateTimeField(auto_now=True)

    # Give's name in admin page
    def __str__(self):
        string = str(self.owner) + " " + self.coin_type
        return string


class HistoryStock(models.Model):
    price = models.DecimalField(max_digits=13, decimal_places=2)
    coin_type = models.CharField(max_length=10)
    date_entered = models.DateTimeField()

    # Gives clear name in admin page
    def __str__(self):
        return self.coin_type

class SavedStock(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    coin_type = models.CharField(max_length=10)

    # Gives clear name in admin page
    def __str__(self):
        string = str(self.owner) + " " + self.coin_type
        return string
