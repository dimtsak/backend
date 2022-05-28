from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from enum import IntEnum

class AbstractProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100,blank=False,null=False,verbose_name='Product Name')
    commercial_name = models.CharField(max_length=100,blank=False,null=False,verbose_name='Commercial Name')
    image = models.ImageField(null=True, blank=True,default='/placeholder.png')
    price = models.FloatField(blank=False,null=False,verbose_name='product Price')
    description = models.TextField(blank=True,null=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    number_of_reviews =  models.IntegerField(null=True, blank=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name:{self.name}-Price:{self.price}$-Description:{self.description}'

    class Meta:
        abstract = True
        
class Product(AbstractProduct):
    class Category(IntEnum):
        BEVERAGE = 1
        SUPPLEMENT = 2
        NUTRITION_PRODUCT = 3

        @classmethod
        def choices(cls):

            return tuple((i.value,i.name) for i in cls)

    category = models.IntegerField(choices = Category.choices(),verbose_name='Category',default=1)

    proteins = models.IntegerField(default=0)
    calories = models.IntegerField(default=0,verbose_name='calories per 100 g')
    is_diab = models.BooleanField(default= False,verbose_name='Suitable for Diabetics') 

    def suitable_for_diabetes(self):
        if self.is_diab == True:
            return 'Suitable for diabetics' 
        else:
            return ' '

    def cat_value(self):
        cat = self.category

        return getattr(self,cat)

    def __str__(self):
        return f'Name:{self.name} -Price:{self.price}$-Calories:{self.calories} cals per 100 g/ml {self.proteins}g  {self.suitable_for_diabetes()}'

    class Meta:
        abstract = False

class Moderator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_moderator = models.BooleanField(default=False)

class Review(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)
