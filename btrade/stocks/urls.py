from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.stocks),
    url(r'^buystock/(?P<pk>\w+)/$', views.buystock)
]
