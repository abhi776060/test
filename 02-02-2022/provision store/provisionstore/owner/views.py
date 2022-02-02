
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Credential,Items,Authentication
from django.contrib.auth import authenticate,login,logout





# Create your views here.


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
        user=Credential.objects.get(email=email,password=password)
        
        if user:
            
            context={'data':user.email}
            return render(request,'home.html',context=context)
        else:
            messages.error(request,' No such users')


    return render(request,'signin.html')
def signout(request):
    
    logout(request)
    return redirect('signin')
    
    
    

def home(request):
    if request.method== 'POST':
        val=request.POST['add']
        
        id1=request.POST['id1']

        if val=='add1':
            name=request.POST['name']
            price=request.POST['price']
            quantity=request.POST['quantity']
            item1=Items.objects.filter(name=name).first()
            if item1:
                item1.quantity=quantity
                if not price :
                    pass
                else:
                    item1.price=price
                item1.save()
                return redirect('home')
            else:



                item=Items(name=name,price=price,quantity=quantity)
                item.save()
                return redirect('home')
            
        if val=='delete1':

            item=Items.objects.filter(id=id1).all()
            item.delete()
            return redirect('home')
        

       

       

    else:
        item=Items.objects.all()
        context={'data':item}
        return render(request,'home.html',context=context)

