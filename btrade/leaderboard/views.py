from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'leaderboard/home.html')
