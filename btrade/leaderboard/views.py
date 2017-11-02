from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import UserProfile

# Create your views here.
def home(request):
    users = User.objects.order_by('-userprofile__earned_currency')
    return render(request, 'leaderboard/home.html', {'users': users})
