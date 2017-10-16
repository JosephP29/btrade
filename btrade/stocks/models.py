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
