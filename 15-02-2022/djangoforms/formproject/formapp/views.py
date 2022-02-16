

from multiprocessing import context
from django.shortcuts import redirect, render,HttpResponse

from formapp.models import Student,Item
from django.contrib import messages
from formapp.form import SignInInputs,SignUpInputs
from django.contrib.sessions.models import Session



# Create your views here.
class SignIn:
    def signin(request):
        
        temp={}
        temp['form']=SignInInputs()
        if request.method=='POST':
            email=request.POST['email']
            password1=request.POST['password']
            user=Student.objects.filter(email=email,password1=password1).first()
            if user :
                request.session['name']=user.email
                return redirect('home')
               
            else:

                messages.error(request,'please check email or password')
                return redirect('signin')
        return render(request,'signin.html',temp)
class SignUp:
    def signup(request):
        temp={}
        temp['form']=SignUpInputs()
        if request.method=='POST':
            name1=request.POST['first_name']
            name2=request.POST['second_name']
            password1=request.POST['password1']
            password2=request.POST['password2']
            email=request.POST['email']
            
            user=Student(first_name=name1,second_name=name2,email=email,password1=password1)
    
            if password1==password2:
                if email not in Student.objects.filter(email=email):

                    user.save()
                    return redirect('signin')
                else:
                     messages.error(request,"email already exists")
                     return redirect('signup')
            else:
                messages.error(request,"wrong password ")
                return redirect('signup')
        return render(request,'signup.html',temp)
class Home:
    def home(request):
        context={}
        context['name']=request.session.get('name')
        product=Item.objects.all()
        context['product']=product

        if request.method=="POST":
            na=request.POST.get('a',None)
            request.session['name']=''
            context['name']=request.session.get('name')
            return redirect('signin')
        else:
            return render(request,'home.html',context)

    
def item(request,id:int):
    
    context={}
    name=request.session.get('name')
    context['name']=name
    product=Item.objects.filter(item_id=id).first()
    context['product']=product
    return render(request,'item.html',context)


    

