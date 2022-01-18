from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=User.objects.filter(email=email)
        print(user)
    
       
    return render(request,'login.html')

def view(request):
     return render(request,'view.html')
