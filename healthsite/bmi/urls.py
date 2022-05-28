from django.urls import path
from .views import home, plooot

urlpatterns = [
    path('bmir', home, name="bmi"),
    path('trackdown',plooot,name= 'track_down'),
    
]
