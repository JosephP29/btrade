from django.db import models
from django.utils import timezone
from btrade import settings

# Create your models here.
class Stock(models.Model):
    #stock = models.IntegerField()
    price = models.PositiveIntegerField()
    supply = models.PositiveIntegerField()
    curr_type = models.CharField(max_length=10, unique=True)
    date_entered = models.DateTimeField()

    def __str__(self):
        return self.curr_type
