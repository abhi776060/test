
from django.urls import path,include
from newzapp import views

urlpatterns = [
    
    path('news',views.newz,name='newz'),

    path('news/<str1>',views.discription,name='discription'),   

   
]
