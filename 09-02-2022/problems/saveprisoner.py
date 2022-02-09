def saveThePrisoner(n, m, s):
    # Write your code here
    list1=[]
    i=s
    j=0
    while j <m:
        j+=1
        list1.append(i)
        if i <n:
            i+=1
        else:
            i=1
    print(list1[-1])

# saveThePrisoner(7,19,2)
# saveThePrisoner(3,7,3)
# saveThePrisoner(5,2,1)
# saveThePrisoner(5,2,2)
# saveThePrisoner(7,19,2)
saveThePrisoner(3,7,3)
