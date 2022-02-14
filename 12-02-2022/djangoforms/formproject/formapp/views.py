

from django.shortcuts import redirect, render,HttpResponse
from formapp.models import Student
from django.contrib import messages
from formapp.form import SignInInputs,SignUpInputs



# Create your views here.
class SignIn:
    def signin(request):
        print(request)
        temp={}
        temp['form']=SignInInputs()
        if request.method=='POST':
            email=request.POST['email']
            password1=request.POST['password']
            user=Student.objects.filter(email=email,password1=password1).first()
            if user :
                first=user.first_name
                second=user.second_name
                context={'first':first,'second':second}
                return render(request,'home.html',context)
               
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
        return render(request,'home.html')



    

