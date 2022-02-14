from django.urls import path,include
from . import views

urlpatterns = [
    path('signin',views.SignIn.signin,name='signin'),
    path('signup',views.SignUp.signup,name='signup'),
    path('home',views.Home.home,name='home'),  

    
]
