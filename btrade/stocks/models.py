from django.db import models
from django.utils import timezone
from btrade import settings
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    price = models.PositiveIntegerField()
    curr_type = models.CharField(max_length=10, unique=True)
    date_entered = models.DateTimeField()

    # Gives clear name in admin page
    def __str__(self):
        return self.curr_type

class User_Stock(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    units = models.PositiveIntegerField()
    #price_bought_at = models.PositiveIntegerField()
    stock_curr_type = models.CharField(max_length=10)
    date_bought = models.DateTimeField(auto_now=True)
    #date_sold = models.DateTimeField(null=True, blank=True)
    #sold = models.BooleanField(default=False)
    #price_sold_at = models.PositiveIntegerField(default=0)

    # Gives clear name in admin page
    def __str__(self):
        string = str(self.owner) + " " + self.stock_curr_type
        return string

class BuyReceipt(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    units = models.PositiveIntegerField()
    price_bought_at = models.PositiveIntegerField()
    curr_type = models.CharField(max_length=10)
    date_bought = models.DateTimeField(auto_now=True)

    # Give's clear name in admin page
    def __str__(self):
        string = str(self.owner) + " " + self.curr_type
        return string

class SellReceipt(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    units = models.PositiveIntegerField()
    price_sold_at = models.PositiveIntegerField()
    curr_type = models.CharField(max_length=10)
    date_bought = models.DateTimeField(auto_now=True)

    # Give's name in admin page
    def __str__(self):
        string = str(self.owner) + " " + self.curr_type
        return string
