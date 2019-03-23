from django.shortcuts import render


from django.shortcuts import render
from django.http import HttpResponse
import django
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from send_email.forms import ContactForm
from send_email.forms import ContactForm_phone
from django.contrib import auth


def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject'], form.cleaned_data['sender']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']
            recepients = ['tokarey003@gmail.com']
            
            try:
                send_mail(subject, message, 'ossdoker@gmail.com', recepients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm()
    return render(reguest, 'contactForm_page/contact.html', {'form': form, 'username': auth.get_user(reguest).username})



def contactform_phone(reguest):
    if reguest.method == 'POST':
        form = ContactForm_phone(reguest.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            sender = form.cleaned_data['phone']
            recepients = ['tokarey003@gmail.com']
            
            try:
                send_mail(subject, sender, 'ossdoker@gmail.com', recepients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm()
    return render(reguest, 'contactForm_page/contact_phone.html', {'form': form, 'username': auth.get_user(reguest).username})



def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'contactForm_page/thanks.html', {'thanks': thanks})