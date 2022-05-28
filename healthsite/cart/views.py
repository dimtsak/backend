from django.shortcuts import render, redirect
from matplotlib.font_manager import findSystemFonts
from .models import *
from cart.form import OrderForm
from store.validations import *
from store.serializers import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def cart(request):
    product = Product.objects.all()
    items = MyBasketProduct.objects.filter(user=request.user)
    frequencies = {}

    total = 0
    for i in items:
        frequencies[i.product.name] = 0
        messages.success(request,"added to cart")
    for i in items:
        total += i.product.price
        frequencies[i.product.name] += 1

    Basketitems = items.count()

    context = {
        'product': product,
        'Basketitems': Basketitems,
        'total': total,
        'frequencies': frequencies,
    }

    return render(request, 'cart/cart.html', context)


def checkout(request):
    items = MyBasketProduct.objects.all()
    frequencies = {}
    total = 0
    for i in items:
        frequencies[i.product.name] = 0
    for i in items:
        total += i.product.price
        frequencies[i.product.name] += 1
    Basketitems = items.count()
    context = {
        'Basketitems': Basketitems,
        'total': total,
        'frequencies': frequencies,
    }
    return render(request, 'cart/checkout.html', context)

@login_required(login_url='login')
def add_product_to_basket(request, id):
        product = Product.objects.get(id=id)
        if request.user.is_authenticated:
            new = MyBasketProduct(product=product,user=request.user)
            new.save()
            return redirect('cart')
        return redirect('registration')


def remove_product_from_basket(request, id):
    product = Product.objects.get(id=id)
    if request.user.is_authenticated:
        new = MyBasketProduct.objects.filter(product=product,user=request.user)
        if new:
            new = new[0]
        new.delete()
        return redirect('cart')
    return redirect('registration')

@login_required(login_url='login')
def order(request):
    errors={}
    items = MyBasketProduct.objects.filter(user=request.user)
    frequencies = {}
    total = 0
    for i in items:
        frequencies[i.product.name] = 0
    for i in items:
        total += i.product.price
        frequencies[i.product.name] += 1
    Basketitems = items.count()

    if total >= 100:
        total*=0.9

    form = OrderForm()
    if request.method == 'POST':
        form=OrderForm(request.POST)

        firstname = request.POST.get('firstname')
        digits_in_fname = checkForDigits(firstname)    
        if digits_in_fname:
            errors['Digits'] = 'No digits allowed in first name!'
            errors['form'] = form
            return render(request,'cart/order.html',errors)

        lastname= request.POST.get('lastname')
        digits_in_lastname = checkForDigits(lastname)

        if digits_in_lastname:
            errors['Digits'] = 'Not digits in last name!'
            errors['form'] = form
            return render(request,'cart/order.html',errors)

        zipcode = request.POST.get('zipcode')

        letters_in_zipcode = checkForLetters(zipcode)
        if letters_in_zipcode:
            errors['Letters'] = letters_in_zipcode
            errors['form'] = form
            return render(request,'cart/order.html',errors)

        too_short_zipcode = smallLength(zipcode,5)
        if too_short_zipcode:
            errors['Small'] = too_short_zipcode
            errors['form'] = form
            return render(request,'cart/order.html',errors)
    
        too_big_zipcode= bigLength(zipcode,5)
        if too_big_zipcode:
            errors['Big'] = too_big_zipcode
            errors['form'] = form
            return render(request,'cart/order.html',errors)
        if form.is_valid():
            form.save()

    context = { 'form':form,
                'items':items,
                'frequencies': frequencies,
                'total': total,
                'Basketitems':Basketitems,}
    return render(request,'cart/order.html',context)