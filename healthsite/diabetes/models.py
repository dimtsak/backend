from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField

from bmi.models import Bmi
# Create your models here.


'''class DiabCheck(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    glucose = models.DecimalField(max_digits=7,decimal_places=2)
    blood_pressure = models.PositiveIntegerField()
    insuline = models.PositiveIntegerField()
    bmi = models.PositiveIntegerField(Bmi.bmi)
    pregnancies = models.PositiveIntegerField()
    skin_thickness = models.FloatField()
    dpf = models.FloatField()
    
    has_diab = models.BooleanField(default=False)
    
    date = models.DateField(auto_now_add=True) '''
    
