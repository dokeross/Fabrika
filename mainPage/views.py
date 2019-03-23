from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *
from .models import Reviews

def main_page(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()

    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_items = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__new_items=True).order_by("-id")[:4]
    hit_items = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__hit_items=True).order_by("-id")[:4]
    reviews = Reviews.objects.filter(is_active=True).order_by("-id")

    return render(request, 'mainPage/main.html', locals())
