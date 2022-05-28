from django.shortcuts import redirect, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

def info(request):
    return render(request, "diabetes/info.html",{})
    
def predict(request):
    diabetes = pd.read_csv(r'diabetes/diabetes.csv')
    X_train, X_Test, y_train,y_test = train_test_split(diabetes.loc[:,diabetes.columns != 'Outcome'],diabetes['Outcome'],stratify=diabetes['Outcome'],test_size=0.28,random_state=66)
    
    forest = RandomForestClassifier(n_estimators=100, random_state=0)
    forest.fit(X_train, y_train)
    result = ' '
    if request.method=="POST":
        print('post works')
        if request.POST.get('age'):
            print(f'val1 works')
            val1 = request.POST.get('age')     
        else:
            val1 =0
            print('val1 doesnt work')    
        val2 = request.POST.get('glucose')
        val3 = request.POST.get('bp')
        val4 = request.POST.get('skin')*10
        val5 = request.POST.get('insulin')  
        val6 = request.POST.get('pedigree')
        val7 = request.POST.get('bmi')
        val8 =request.POST.get('pregnancies')
        pred = forest.predict([[float(val1),float(val2),float(val3),float(val4)*10,float(val5),float(val6)*0.1,float(val7),float(val8)]])
        if pred ==[1]:
            result ='Positive'
        else:
            result='Negative'
    return render(request,"diabetes/index.html",{'result':result})

def create_value(request,val,message):
    errors = {}
    if request.method=="POST":
        value = request.POST.get(val)
        try :
            valuef = float(value)
        except ValueError:
            errors['Invalid'] = message
            return message
        
        return(value)

def check_if_in_list(char,list_checked):
    if char not in list_checked:
        return f'You should choose a number from {list_checked}'

def predict(request):
    
    diabetes = pd.read_csv(r'diabetes/diabetes.csv')

    errors = {}
    
    X_train, X_Test, y_train,y_test = train_test_split(diabetes.loc[:,diabetes.columns != 'Outcome'],diabetes['Outcome'],stratify=diabetes['Outcome'],test_size=0.28,random_state=66)
    
    forest = RandomForestClassifier(n_estimators=100, random_state=0)
    forest.fit(X_train, y_train)
    result = ' '
    if request.method=="POST":
        
        val1 = request.POST.get('age')
        
     
            
        val2 = request.POST.get('glucose')
        try :
            val2f = float(val2)
        except ValueError:
            errors['Invalid'] = 'Invalid input!You should give a number for glucose levels! '
            return render(request,'diabetes/index.html',errors)
        #except Exception as e:
            
        if val2f <50 or val2f>350 :
            errors['Invalid'] ='You cant\'t give this number for your glucose levels!'
            return render(request,'diabetes/index.html',errors)
        
        try:
            val3 = float(request.POST.get('bp'))
        except ValueError:
            errors['Invalid'] = 'Invalid input!You should give a number for glucose levels! '
            return render(request,'diabetes/index.html',errors)
        #if val2f <50 or val2f>300 :
         #   errors['Invalid'] ='You cant\'t give this number for your glucose levels!'
          #  return render(request,'diabetes/index.html',errors)
        
    
        val4 = request.POST.get('skin')
        skin_list = ['1','2','3']
        if val4 not in skin_list:
            errors['invalid'] = 'You should choose 1 or 2 or 3 for skin thickness!'
            return render(request,"diabetes/index.html",errors)
        val4 =val4*10
        val5 = create_value(request,'insulin','Not valid for insulin levels!')
        #request.POST.get('insulin')
        errors[val5] = 'Invalid insulin! '
        val6 = request.POST.get('pedigree')
        pedigree_list = ['0','1','2']
        if val6 not in pedigree_list:
            errors['invalid'] = 'You should choose 0 or 1 or 2!'
            return render(request,"diabetes/index.html",errors)
        val7 = create_value(request,'bmi','Not valid for bmi levels!')
        #request.POST.get('bmi')
        val8 =request.POST.get('pregnancies')
        if not val8.isdigit() :
            errors['invalid'] = 'You should give a positive number or 0 for pregnancies!'
            return render(request,"diabetes/index.html",errors)
            
        try:
            pred = forest.predict([[float(val1),val2f,float(val3),float(val4)*10,val5,float(val6)*0.1,float(val7),float(val8)]])
        except ValueError:
            errors['invalid'] = 'Invalid Input!See the instructions and try again!'
            return render(request,"diabetes/index.html",errors)
        
        if pred ==[1]:
            result ='Positive'
        else:
            result='Negative'
    
    return render(request,"diabetes/index.html",{'result':result})

#-------------------------------For further Devlopment----------------------------------------

def predict2(request):
    diabetes = pd.read_csv(r'diabetes/diabetes.csv')
    context = {}
    errors = {} 
    X_train, X_Test, y_train,y_test = train_test_split(diabetes.loc[:,diabetes.columns != 'Outcome'],diabetes['Outcome'],stratify=diabetes['Outcome'],test_size=0.28,random_state=66) 
    forest = RandomForestClassifier(n_estimators=100, random_state=0)
    forest.fit(X_train, y_train)
    result = ' '
    if request.method=="POST":
        val1 = create_value(request,'age','Not valid input for age!')
        val2 = create_value(request,'glucose','Not valid input for glucose levels!')
        val3 = create_value(request,'bp','Not valid input for your blood pressure!')
        val4 = request.POST.get('skin')
        skin_list = ['1','2','3']
        skin_not_in_list = check_if_in_list(val4,skin_list)
        
        
        if skin_not_in_list :
            errors['listError'] = f'For skin thickness: {skin_not_in_list}'
            return render(request,"diabetes/index.html",errors)
        
        val5 = create_value(request,'insulin','Not valid input for insulin levels!')
        val6 = request.POST.get('pedigree')
        pedigree_list = ['0','1','2']
        pedigree_not_in_list = check_if_in_list(val6,pedigree_list)
        
        
        if pedigree_not_in_list:
            errors['listError'] = f'For pedigree: {pedigree_not_in_list}'
            return render(request,"diabetes/index.html",errors)
        val7 = create_value(request,'bmi','Not valid input for bmi!')
        val8 = create_value(request,'pregnancies','Not valid input for pregnancies!')
        values = [val1,val2,val3,val4,val5,val6,val7,val8]
        for val in values:
            try:
                val = float(val)
            except ValueError:
            
                errors['Invalid'] = val
                return render(request,"diabetes/index.html",errors)
            except Exception as e:
                errors['e'] = "Something went really wrong!Try again!"
                return render(request,"diabetes/index.html",errors)
        
    
        pred = forest.predict([[val1,val2,val3,float(val4)*10,val5,float(val6)*0.1,val7,val8]])
        
        if pred ==[1]:
            result ='Positive'
        else:
            result='Negative'
   
    
    return render(request,"diabetes/index.html",{'result':result})

