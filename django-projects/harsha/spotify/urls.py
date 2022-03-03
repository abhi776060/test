from django.urls import path,include
from spotify import views

urlpatterns = [
    
    path('',views.play,name='play'),

    # path('/<str1>',views.discription,name='discription'),   

   
]
