
from django.urls import path
from register import views

urlpatterns = [
    path('',views.login, name='login'),
    path('',views.view, name='view'),
]