from .views import *
from django.urls import path

urlpatterns =[
    path('predict',predict,name='predict'),
    path('predict2',predict2,name='predict2'),
    path('info',info,name='info'),
    
    
]