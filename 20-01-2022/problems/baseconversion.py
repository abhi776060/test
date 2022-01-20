def myfun(top,bottom):
    num=top
    list1=[]
    while True:
        
        a=num%bottom
        list1.append(a)
        num=int(num/bottom)
        if num < bottom:
            list1.append(num)
            break
    if bottom == 16:
        list2=[]
        list_hexa_value={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        for x in list1:
            if x <=9 :
                list2.append(x)
            else:
                list2.append(list_hexa_value[x])


    print(list2[::-1])
        
myfun(5695464,16)