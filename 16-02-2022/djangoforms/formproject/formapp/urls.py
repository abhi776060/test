from django.urls import path
from . import views

urlpatterns = [
    path('signin',views.SignIn.signin,name='signin'),
    path('signup',views.SignUp.signup,name='signup'),
    path('home',views.Home.home,name='home'),  
    path('<int:id>',views.item,name='item'),  
    path('update',views.update,name='update'),  
    path('add',views.add,name='add'),  
    
]
