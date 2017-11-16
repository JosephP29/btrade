from django.db import models
from django.utils import timezone
from btrade import settings
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    price = models.PositiveIntegerField()
    coin_type = models.CharField(max_length=10, unique=True)
    date_entered = models.DateTimeField()

    # Gives clear name in admin page
    def __str__(self):
        return self.coin_type


class current_price_table(models.Model):
    time = models.DateTimeField('%Y-%m-%d %H:%M:%S')
    coin_type = models.CharField(max_length=10, unique=True)
    price = models.FloatField()
    volume = models.FloatField()
    mktcap = models.FloatField()

    # Gives clear name in admin page
    def __str__(self):
        return self.coin_type


class history(models.Model):
    time = models.DateTimeField('%Y-%m-%d %H:%M:%S')
    coin_type = models.CharField(max_length=10)
    price = models.FloatField()
    volume = models.FloatField()
    mktcap = models.FloatField()

    # Gives clear name in admin page
    def __str__(self):
        return self.coin_type

class User_Stock(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    units = models.FloatField()
    #price_bought_at = models.PositiveIntegerField()
    coin_type = models.CharField(max_length=10)
    date_bought = models.DateTimeField(auto_now=True)
    netgain = models.FloatField(default=0.00)
    #date_sold = models.DateTimeField(null=True, blank=True)
    #sold = models.BooleanField(default=False)
    #price_sold_at = models.PositiveIntegerField(default=0)

    # Gives clear name in admin page
    def __str__(self):
        string = str(self.owner) + " " + self.coin_type
        return string

class BuyReceipt(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    units = models.FloatField()
    price_bought_at = models.FloatField()
    coin_type = models.CharField(max_length=10)
    date_bought = models.DateTimeField(auto_now=True)

    # Give's clear name in admin page
    def __str__(self):
        string = str(self.owner) + " " + self.coin_type
        return string

class SellReceipt(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    units = models.FloatField()
    price_sold_at = models.FloatField()
    coin_type = models.CharField(max_length=10)
    date_bought = models.DateTimeField(auto_now=True)

    # Give's name in admin page
    def __str__(self):
        string = str(self.owner) + " " + self.coin_type
        return string


class HistoryStock(models.Model):
    price = models.PositiveIntegerField()
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
