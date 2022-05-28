from django.shortcuts import render
from .models import *
from abc import ABCMeta as am,abstractmethod

class ShowProducts(metaclass=am):
    @abstractmethod
    def showProducts(self):
        pass

class ShowAllProducts(ShowProducts):
    def showProducts(self,request):
        products = Product.objects.all().order_by('price')
        context={
            'products':products
        }
        return render(request,'store/products.html',context)
        
class ShowSupplements(ShowProducts):
    def showProducts(self,request):
        product_list = Product.objects.all().order_by('price')
        sup_list = [i for i in product_list if i.category == 2]
        context = {'sup_list':sup_list}
        return render(request,'store/sup.html',context)

class ShowBev(ShowProducts):
    def showProducts(self,request):
        product_list = Product.objects.all().order_by('price')
        bev_list = [i for i in product_list if i.category == 1]
        context = {'bev_list':bev_list}
        return render(request,'store/bev.html',context)
    
class ShowNutri(ShowProducts):
    def showProducts(self,request):
        product_list = Product.objects.all().order_by('price')
        nutri_list = [i for i in product_list if i.category == 3 ]
        context = {'nutri_list':nutri_list}
        return render(request,'store/nutri.html',context)
    
class ShowLowCal(ShowProducts):
    def showProducts(self,request):
        product_list = Product.objects.all()
        lowcal_list = [i for i in product_list if i.calories <80]
        context = {'lowcal_list':lowcal_list}
        return render(request,'store/lowcal.html',context)

class ShowDiab(ShowProducts):
    def showProducts(self,request):
        product_list = Product.objects.all()
        diabetic_list = [i for i in product_list if i.is_diab == True]
        context = {'diabetic_list':diabetic_list}
        return render(request,'store/diabetic.html',context)

class ShowProt(ShowProducts):
    def showProducts(self,request):
        product_list = Product.objects.all()
        protein_list = [i for i in product_list if i.proteins>12]
        context = {'protein_list':protein_list}
        return render(request,'store/protein.html',context)

