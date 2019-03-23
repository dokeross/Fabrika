from django import forms
from .models import *


class ProductCommentsForm(forms.ModelForm):

    class Meta:
        model = ProductComments
        exclude = [""]