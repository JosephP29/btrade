from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.stocks),
    url(r'^trending', views.trending),
	url(r'^stockdetail/(?P<coin_type>\w+)/$', views.stockdetail),
	url(r'^buystock/(?P<coin_type>\w+)/$', views.buystock),
	url(r'^sellstock/(?P<coin_type>\w+)/$', views.sellstock),
	url(r'^savestock/(?P<coin_type>\w+)/$', views.savestock),
	url(r'^unsavestock/(?P<coin_type>\w+)/$', views.unsavestock),
]
