from django.urls import path,include
from calapp import views

urlpatterns = [
    
    path('',views.calculate,name='calculate'),
    path('advance',views.calculate1,name='calculate1'),



   
]
