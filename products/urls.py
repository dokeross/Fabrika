from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    url(r'^like_adding/$', views.like_adding, name='like_adding'),
]
