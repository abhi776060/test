from django.shortcuts import render
t=''
# Create your views here.
def view(request):
    result=''
    value=''
    global t
    if request.method == 'POST':
        value1=request.POST.get('v1')
        if value1=='q':
            a=value
        else:
            
            t.append(value1)
        for o in t:
            value+=o
        
       
        
        
        print(a)  
        try:
            if "+" in a:
                str1=a.split("+")
                if len(str1)<=2:
                    print(str1)
                    for x in str1:
                        value.append(float(x))
                    sum=float(value[0])+float(value[1])                
                    result1=str(sum)
                    result=verify(result1)
                    print(result)
                else:
                    result=" sorry!!It will perform only on single operator "
            elif "-" in a:
                str1=a.split("-")
                if len(str1) <=2:
                    print(str1)
                    for x in str1:
                        value.append(float(x))
                    sum=float(value[0])-float(value[1])
                    result1=str(sum)
                    result=verify(result1)
                    print(result)
                else:
                    result=" sorry!!It will perform only on single operator "
            elif "**" in a:
                str1=a.split("**")
                if len(str1)<=2:
                    print(str1)
                    for x in str1:
                        value.append(float(x))
                    sum=float(value[0])**float(value[1])
                    result1=str(sum)
                    result=verify(result1)
                    print(result)
                else:
                    result=" sorry!!It will perform only on single operator "
            
            elif "*" in a:
                str1=a.split("*")
                if len(str1)<=2:
                    print(str1)
                    for x in str1:
                        value.append(float(x))
                    sum=float(value[0])*float(value[1])
                    result1=str(sum)
                    result=verify(result1)
                    print(result)
                else:
                    result=" sorry!!It will perform only on single operator "
            elif "//" in a:
                str1=a.split("//")
                print(str1)
                if len(str1) <=2:
                    for x in str1:
                        value.append(float(x))
                    sum=float(value[0])//float(value[1])
                    result=str(sum)
                    
                    print(result)
                else:
                    result=" sorry!!It will perform only on single operator "
            elif "/" in a:
                str1=a.split("/")
                if len(str1)<=2:
                    print(str1)
                    for x in str1:
                        value.append(float(x))
                    sum=float(value[0])/float(value[1])
                    result=str(sum)
                    print(result)
                else:
                    result=" sorry!!It will perform only on single operator "
            elif "%" in a:
                str1=a.split("%")
                if len(str1) <=2:
                    print(str1)
                    for x in str1:
                        value.append(float(x))
                    sum=float(value[0])%float(value[1])
                    result1=str(sum)
                    result=verify(result1)
                    print(result)
                else:
                    result=" sorry!!It will perform only on single operator "
        
            else:
                result="Error"
        except:
            result='Error'
    
            
    return render(request,'basiccal/calculator.html',{'data':result,'o':value})

def verify(str1):
    index=str1.split(".")
    if int(index[1]) ==0:
        return index[0]
    else:
        return str1 