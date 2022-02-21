
from django.shortcuts import redirect, render,HttpResponse

from formapp.models import Student,Item
from django.contrib import messages
from formapp.form import SignInInputs,SignUpInputs,FormItem

# Create your views here.
class SignIn:
    def signin(request):
        temp={}
        temp['name']=request.session.get('name')
        temp['form']=SignInInputs()
        if request.method=='POST':
            email=request.POST['email']
            password1=request.POST['password']
            user=Student.objects.filter(email=email,password1=password1).first()
            if user :
                request.session['name']=user.email
                request.session['username']=user.first_name
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
        context['username']=request.session.get('username')
        product=Item.objects.all()
        context['product']=product

        if request.method=="POST":
            logout=request.POST.get('logout')
            itemid=request.POST.get('itemid')
            submit=request.POST.get('submit')

            if logout:
                request.session['name']=''
                context['name']=request.session.get('name')
                return redirect('signin')
            if itemid:
                item=Item.objects.filter(item_id=int(itemid)).first()
                context['item']=item
                return render(request,'home.html',context)
        else:
            return render(request,'home.html',context)

    
def item(request,id:int):
    
    context={}
    name=request.session.get('name')
    context['name']=name
    product=Item.objects.filter(item_id=id).first()
    context['product']=product
    return render(request,'item.html',context)


def base(request):
    return render(request,'base.html') 

def update(request):
    context={}
    context['name']=request.session.get('name')
    context['form']=FormItem()
    if request.method== "POST":
            input_data=request.POST['find']
            
            if input_data == 'Submit':
                id=request.POST.get('id')
                item=Item.objects.filter(item_id=int(id)).first()
                try:
                    item.item_id
                    context['item']=item
                    context['id']=id
                except:
                    messages.success(request,f"id {id} not found")
                    return redirect('update')

            if input_data =='update':
                try:
                    id=request.POST.get('id')
                    item1=Item.objects.filter(item_id=id).first()
    
    
                    name1= request.POST.get('name')
                    price1= request.POST.get('price')
                    img1= request.POST.get('img')
                    discription1= request.POST.get('discription')
                    item1.name=name1
                    item1.price=price1
                    item1.img=img1
                    item1.discription=discription1
                    item1.save()
                    messages.success(request,f"id {id} updated")
                    return redirect('update')

                except:
                     messages.error(request,f"no such {id}")
                     return redirect('update')
    return render(request,'update.html',context) 

def add(request):
    context={}
    context['name']=request.session.get('name')
    return render(request,'add.hmtl',context)

