from cgi import test
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .models import Credential,Items

# Create your views here.

def display(request):
    return HttpResponse("welcome to sachin provisionstore")

def signup(request):
    if request.method =='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 == pass2:
            user=Credential.objects.filter(email=email).all
            try:
                if user:
                    new_user=Credential(first_name=fname,last_name=lname,email=email,password=pass1)
                    new_user.save()
            except:
                messages.error(request,'user already there :')
        else:
            messages.error(request,'password wrong')


    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        email=request.POST['email']


    return render(request,'signin.html')

def signout(request):
    pass

def home(request):
    return render(request,'home.html')

