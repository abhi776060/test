from multiprocessing import context
from django.shortcuts import render

str1=''
# Create your views here.
def calculate(request):
    context={}
    if request.method=="POST":
        expression=request.POST['cal']
        try:
           sum=eval(expression)
           
           context['data']=sum
        except:
            context['data']="ERRor"
    return render(request,'cal.html',context=context)
def calculate1(request):
    context={}
    global str1
    if request.method=="POST":
        expression=request.POST['data']
        str1+=expression
        context['up']=str1
        try:
            if '=' in str1:
                result=eval(str1[:-1])
                context['up']=result
                str1=''
        except:
            context['up']='ERROR'
            str1=''
        
        if 'c' in str1:
            str1=''
            context['up']=str1

    return render(request,'advance.html',context=context)