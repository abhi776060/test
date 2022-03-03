from django.urls import path
from botapp import views

urlpatterns = [
    
    path('',views.message,name='message'),
    
   

   
]
