from django.shortcuts import render
# from products.models import *


def about(request):
    return render(request, 'about/about.html', locals())