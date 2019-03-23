from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    url(r'^order/$', views.order, name='order'),
]