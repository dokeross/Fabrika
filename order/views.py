from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import *

from django.shortcuts import render
from .forms import OrderContactForm
from django.contrib.auth.models import User

from django.shortcuts import render



from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from send_email.forms import ContactForm
from send_email.forms import ContactForm_phone
from django.contrib import auth

def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print (request.POST)
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    image = data.get("image")
    is_delete = data.get("is_delete")
    # product = Product.objects.get(id=product_id)
    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     is_active=True, image=image, defaults={"nmb": nmb})
        if not created:
            print ("not created")
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)
    #common code for 2 cases
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["category"] = item.product.category.name
        product_dict["article"] = item.product.article
        product_dict["measurement"] = item.product.measurement
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        product_dict["image"] = str(item.image)
        return_dict["products"].append(product_dict)
    
    return JsonResponse(return_dict)

def order(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form = OrderContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print("yes")
            data = request.POST
            name = data.get("name")
            phone = data["phone"]
            last_name = data["last_name"]
            customer_email = data["email"]
            comments = data["comments"]
            index = data["index"]
            city = data["city"]
            street = data["street"], data["streetekb"]
            house = data["house"], data["houseekb"]
            kv = data["kv"], data["kvekb"]
            time = data["time"]
            check_russia = data.get("check_russia")
            if check_russia:
                check_russia = check_russia
            else:
                check_russia = False
            
            check_ekb = data.get("check_ekb")
            if check_ekb:
                check_ekb = check_ekb
            else:
                check_ekb = False
                
            recepients = ['info.fabrikastore@gmail.com']
            
            try:
                send_mail(name, phone, 'info.fabrikastore@gmail.com', recepients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            # return HttpResponseRedirect('/thanks/')


            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})

            order = Order.objects.create(user=user, customer_index=index, customer_name=name, check_russia=check_russia, check_ekb=check_ekb, customer_city=city, customer_street=street, customer_time=time, customer_house=house, customer_kv=kv, comments=comments, customer_email=customer_email, surname=last_name, customer_phone=phone, status_id=1)

            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    print(type(value))

                    product_in_basket.nmb = value
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_basket.product, nmb = product_in_basket.nmb,
                                                  price_per_item=product_in_basket.price_per_item,
                                                  total_price = product_in_basket.total_price,
                                                  order=order)

            # return HttpResponseRedirect(request.META['HTTP_REFERER'])
            return HttpResponseRedirect('/thanks/')
        else:
            print("no")
        
    return render(request, 'order/order.html', locals())

