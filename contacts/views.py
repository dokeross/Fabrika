from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import *

from django.shortcuts import render
from .forms import ContactsForm_phone
from django.contrib.auth.models import User

from django.shortcuts import render


from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from send_email.forms import ContactForm
from send_email.forms import ContactForm_phone
from django.contrib import auth


# Create your views here.
def contacts_page(request):
    
    form = ContactsForm_phone(request.POST or None)
    if request.POST:
        print(request.POST)
        data = request.POST
        subject = data['name']
        phone = 'appeal from the page contacts'
        recepients = ['info.fabrikastore@gmail.com']
        try:
            print('okok')
            send_mail(subject, phone, 'info.fabrikastore@gmail.com', recepients)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm()


    return render(request, 'contacts/contacts_page.html', locals())
