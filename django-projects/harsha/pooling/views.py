from django.shortcuts import render
from pooling.models import Vote
# Create your views here.
def create(request):
    context={}
    if request.method=="POST":
        question=request.POST['question']
        op1=request.POST['op1']
        op2=request.POST['op2']
        op3=request.POST['op3']
        op4=request.POST['op4']
        v1=request.POST.get('v1',0)
        v2=request.POST.get('v2',0)
        v3=request.POST.get('v3',0)
        v4=request.POST.get('v4',0)
        question1=Vote()
        question1.question=question
        question1.option1=op1
        question1.option2=op2
        question1.option3=op3
        question1.option4=op4
        question1.v1=0
        question1.v2=0
        question1.v3=0
        question1.v4=0
        question1.save()
    
    return render(request,'voting.html',context=context)

def vote(request):
    context={}
    question1=Vote.objects.all()
    context['data']=question1
    if request.method =="POST":
        question=request.POST['question']
        op1=request.POST.get('op1',0)
        op2=request.POST.get('op2',0)
        op3=request.POST.get('op3',0)
        op4=request.POST.get('op4',0)
        ele=Vote.objects.filter(question=question).first()
        print(ele.v1,ele.v2,ele.v3,ele.v4)
        if op1:
            ele.v1+=1
           
        if op2:
            ele.v2+=1
           
        if op3:
            ele.v3+=1
           
        if op4:
            ele.v4+=1
        ele.save()
        result=request.POST.get("result",None)
        if result:
            
            context['result']=(f'{ele.option1}',ele.v1,f'{ele.option2}',ele.v2,f'{ele.option3}',ele.v3,f'{ele.option4}',ele.v4,f'{max(ele.v1,ele.v2,ele.v3,ele.v4)}')
        

        
    
    return render(request,'view.html',context=context)