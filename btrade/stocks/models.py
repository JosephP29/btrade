from django.db import models
from django.utils import timezone
from btrade import settings
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    #id = models.AutoField(primary_key=True)
    price = models.PositiveIntegerField()
    supply = models.PositiveIntegerField()
    curr_type = models.CharField(max_length=10, unique=True)
    date_entered = models.DateTimeField()
    #owner = ForeignKey(User)

    def __str__(self):
        return self.curr_type


class User_Stock(models.Model):
	#id = models.AutoField(primary_key=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	units = models.PositiveIntegerField()
	price_bought_at = models.PositiveIntegerField()
	stock_curr_type = models.CharField(max_length=10)
	date_bought = models.DateTimeField(auto_now=True)
	date_sold = models.DateTimeField(null=True, blank=True)
	sold = models.BooleanField(default=False)
	price_sold_at = models.PositiveIntegerField(default=0)

	#def create(self, )