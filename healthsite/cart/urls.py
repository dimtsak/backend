from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('order/', order, name="order"),
    path('add_product_to_basket/<str:id>/',add_product_to_basket, name="add_to_basket"),
    path('remove_product_from_basket/<str:id>/',remove_product_from_basket, name="remove_product_from_basket"),
]
