from django.urls import path
from . import views

urlpatterns=[
    path('',views.display,name='display'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('home', views.home, name='home'),


   
]