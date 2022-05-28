# from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,authenticate,logout
from flask import request
from .models import *
from .forms import RegistrationForm,ProductForm
from .validations import *
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView,PasswordChangeForm
from django.urls import reverse_lazy
# from rest_framework.response import Response
from .serializers import *
# from rest_framework.decorators import api_view
from rest_framework import viewsets
from .filter import PriceFilter
from django.db.models import Avg, Max, Min

def home(request):
    return render(request,'home.html')

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset=Product.objects.all()

class LowCalViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer        
    queryset = Product.objects.filter(calories__lt=80)

class DiabeticViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_diab=True)

class ProteinViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(proteins__gte=12)

class SupplementViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(category=2)

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('latest_homepage')
    else:
        print('fail')
        form = RegistrationForm()
    context={'form':form}
    return render(request,'store/register.html',context)

def loginpage(request):    
    errors={}
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password = password)
        if user is not None:
            login(request,user)
            return redirect('latest_homepage')
        else:
            if not username:
                errors['empty_username'] = 'Please enter username'
            elif not password:
                errors['empty_password'] = 'Please enter password'
            elif user is None:
                errors['invalid'] = 'Username and Password do not match.'
    return render(request, 'store/login.html', errors)

def logoutuser(request):
	logout(request)
	return redirect('latest_homepage')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm 
    success_url=reverse_lazy('login')

def productslist(request):
    products =Product.objects.all()
    return render(request,'store/products.html',{'products':products})

def singleproduct(request,pk):
    singleproduct =Product.objects.get(id=pk)
    return render(request,'store/singleproduct.html',{'singleproduct':singleproduct})

def adminpanel(request):
    products = Product.objects.all()
    return render (request,'store/admin_panel.html',{'products':products})

def addproduct(request): 
    errors = {}
    product_set = Product.objects.all()      
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        name = request.POST.get('name')
        commercial_name = request.POST.get('commercial_name')
        for product in product_set.iterator():
            if product.commercial_name == commercial_name:
                errors["Existing"] = 'This commercial name already exists!'
                errors['form'] = form
                return render(request,'store/create.html',errors)

        digits_in_name = checkForDigits(name)
        if digits_in_name:
            errors['Digits'] = digits_in_name
            errors['form'] = form
            return render(request,'store/create.html',errors)       

        if form.is_valid():
            form.save()
            return redirect('adminpanel')
    context ={
        'form':form,
    }
    return render(request,'store/create.html',context)

def editproduct(request,pk):
    errors = {}
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        name = request.POST.get('name')
        digits_in_name = checkForDigits(name)
        if digits_in_name:
            errors['Digits'] = digits_in_name
            errors['form'] = form
            return render(request,'store/create.html',errors)

        if form.is_valid():
            form.save()
            return redirect('adminpanel')
    context={
        'form':form
    }
    return render(request,'store/update.html',context)

def deleteproduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('adminpanel')

def filter(request):
    productsfilt = Product.objects.all()

    pricemin = productsfilt.aggregate(Min('price'))
    pricemax = productsfilt.aggregate(Max('price'))
    myFilter = PriceFilter(request.GET, queryset=productsfilt)
    productsfilt = myFilter.qs
    print(pricemin['price__min'])
    print(pricemax['price__max'])

    my_context= {
        'myFilter':myFilter,
        'productsfilt':productsfilt,
        'pricemin':pricemin['price__min'],
        'pricemax':pricemax['price__max'],
    }
    return render(request, 'store/products.html', my_context)

def latest(request):
    today = datetime.today()
    year = today.year
    month = today.month
    
    latest_prod = Product.objects.filter(date_created__year=year, 
        date_created__month=month)  
    
    return render(request, "store/latest.html", {'products': latest_prod})

def latest_homepage(request):
    today = datetime.today()
    year = today.year
    month = today.month
    
    latest_products = Product.objects.filter(date_created__year=year, date_created__month=month)
    lowcal = Product.objects.filter(calories__lt=80) 
    diabetic = Product.objects.filter(is_diab=True) 
    protein = Product.objects.filter(proteins__gte=12)
    
    return render(request, "home.html", {
        'latest_products': latest_products,
        'lowcal': lowcal,
        'diabetic': diabetic,
        'protein': protein
        })

def contact(request):
    return render(request,'store/contact.html')