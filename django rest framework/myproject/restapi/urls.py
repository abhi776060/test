from django.urls import path
from restapi import views


urlpatterns = [
    
    path('article/', views.article_list,name='article'),
    path('article_details/<int:pk>/', views.article_detail,name='article_detail'),
]