def check(arg):
    flag=False
    for x in range(len(arg)-1):
        diff=abs(arg[x]-arg[x+1])
        if diff <=1:
            flag=True
        else:
           flag=False
           break
    return flag

 
    
# print(check([1,1,2,2,4]))
def pickingNumbers(a):
    list1=[]
    for x in range(len(a)):
        for y in range(x+1,len(a)+1):
            if len(a[x:y])>1:
                
                a1=check(a[x:y])
                if a1:
                    list1.append(a[x:y])
    print(list1)
array1=[1,1,2,2,4,4,5,5,5]
array2=[4,6,5,3,3,1]
array3=[98,3,99,1,97,2]
pickingNumbers(array2)



