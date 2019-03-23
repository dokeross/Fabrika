from django import forms
from .models import *


class OrderContactForm(forms.Form):
    
    name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    comments = forms.CharField(required=False)
    index = forms.CharField(required=False)
    city = forms.CharField(required=False)
    city = forms.CharField(required=False)
    street = forms.CharField(required=False)
    streetekb = forms.CharField(required=False)
    house = forms.CharField(required=False)
    houseekb = forms.CharField(required=False)
    kv = forms.CharField(required=False)
    kvekb = forms.CharField(required=False)
    time = forms.CharField(required=False)
    check_russia = forms.BooleanField(required=False)
    check_ekb = forms.BooleanField(required=False)