from django.conf.urls import url, include
from django.contrib import admin
from btrade import views
from leaderboard import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
]
