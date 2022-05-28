from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from store.models import *
from store.forms import*
import re

# alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only characters are allowed.')

def test(val):
    if re.match('0123456789', val):
        raise ValidationError('Disallowed')

class MyBasketProduct(models.Model):
    user = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name}'


class Order(models.Model):
    firstname=models.CharField(max_length=45,blank=False,null=False,validators=[test])
    lastname=models.CharField(max_length=45,blank=False,null=False)
    address=models.CharField(max_length=45,blank=False,null=False)
    number=models.PositiveIntegerField(max_length=45,blank=False,null=False)
    zipcode = models.CharField('Zipcode', max_length=5, validators=[MinLengthValidator(5)])
    city=models.CharField(max_length=45,blank=False,null=False)
    country=models.CharField(max_length=45,blank=False,null=False)

    def __str__(self):
        return f'{self.user.username},{self.firstname},{self.lastname}'

