from django.urls import path,include
from pooling import views

urlpatterns = [

    path('create',views.create,name='create'),
    path('vote',views.vote,name='vote'),




]