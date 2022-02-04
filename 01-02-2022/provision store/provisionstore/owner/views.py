
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Credential,Items



# Create your views here.
def login(arg):
    return arg



def display(request):
    return render(request,"display.html")

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
                    return redirect('signin')
            except:
                messages.error(request,'user already there :')
        else:
            messages.error(request,'password wrong')


    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['pass1']
        new_user=Credential.objects.filter(email=email,password=password).all()
        if new_user:
            context={'data':login(email)}
            return render(request,'home.html',context)
        else:
            messages.error(request,' No such users')


    return render(request,'signin.html')
def signout(request):
    return redirect('signin')
    
    
    

def home(request):
    if request.method== 'POST':
        val=request.POST['value']
        if val == 'add':
            name=request.POST['name']
            price=float(request.POST['price'])
            quantity=float(request.POST['quantity'])
            item=Items(name=name,price=price,quantity=quantity)
            item.save()
            return redirect('home')

        if val == 'edit':
            name=request.POST['name']
            price=float(request.POST['price'])
            quantity=float(request.POST['quantity'])
            item=Items(name=name,price=price,quantity=quantity)
            item.save()
            return redirect('home')

        if val == 'delete':
            name=request.POST['name']
            price=float(request.POST['price'])
            quantity=float(request.POST['quantity'])
            item=Items(name=name,price=price,quantity=quantity)
            item.save()
            return redirect('home')

       

    else:
        item=Items.objects.all()
        context={'data':item}
        return render(request,'home.html',context=context)

