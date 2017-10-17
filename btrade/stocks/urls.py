from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.stocks),
	url(r'^stockdetail/(?P<pk>\w+)/$', views.stockdetail),
	url(r'^confirmbuy/(?P<pk>\w+)/$', views.confirmbuy),
	url(r'^confirmsell/(?P<pk>\w+)/$', views.confirmsell)
]