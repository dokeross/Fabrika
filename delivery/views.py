from django.shortcuts import render
# from products.models import *


def delivery(request):
    return render(request, 'delivery/delivery.html', locals())