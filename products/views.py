from django.shortcuts import render
from .forms import ProductCommentsForm
from products.models import *
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.utils import timezone

from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from send_email.forms import ContactForm
from send_email.forms import ContactForm_phone
from django.contrib import auth

def product(request, product_id):
    
    form = ProductCommentsForm(request.POST or None)
    if request.method == "POST" and form.is_valid():

        return_dict = dict()
        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()
        print (request.POST)
        data = request.POST
        published_date = timezone.now()
        
        name = data.get("name")
        comments = data.get("comments")
        article = data.get("article")
        ProductComments.objects.filter(id=product_id).create(product_id=product_id, published_date=published_date, name=name, comments=comments)

       
        subject = data['name']
        article = data['article']
        recepients = ['info.fabrikastore@gmail.com']
        try:
            print('okok')
            send_mail(subject, article, 'info.fabrikastore@gmail.com', recepients)
        except BadHeaderError:
            return HttpResponse('Invalid header found')

    product = Product.objects.get(id=product_id)
    similarProducts = product.similarproducts_id
    

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)  
    products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category_id=similarProducts) 
    order = product.productimage_set.filter(is_main=True)
    return render(request, 'products/product.html', locals())


def like_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print (request.POST)
    data = request.POST
    like = data.get("like")
    product_id = data.get("product_id")

    Product.objects.filter(id=product_id).update(like=like)
    
    #common code for 2 cases
    products_like = Product.objects.filter(session_key=session_key, id=product_id, is_active=True)

    return_dict["likes"] = list()

    for item in products_like:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["like"] = item.like
        product_dict["liketrue"] = item.likeTrue
        return_dict["likes"].append(product_dict)
    
    return JsonResponse(return_dict)