
from django.urls import path,include
from newzapp import views

urlpatterns = [
    
    path('/',views.newz,name='newz'),

    path('/<str1>',views.discription,name='discription'),   

   
]
