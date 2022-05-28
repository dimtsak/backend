from email.policy import default
from xml.etree.ElementInclude import include
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from store.models import Product

class RegistrationForm(UserCreationForm):
    username = forms.SlugField(max_length=45)

    class Meta:
        model=User
        fields=('username', 'password1', 'password2', 
                'email',)

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        exclude=('user',)