def calculate(arg):
    list1=[]
    count=0
    for x in range(1,arg):
        list2=[]
        for y in range(x,x+7):
            if count <arg:
                count+=1
                list2.append(y)
            else:
                pass
        if list2:
            list1.append(list2)
    print(list1)
    sum=0
    for x in list1:
        for y in x:
            sum+=y
    print(sum)

calculate(20) 
