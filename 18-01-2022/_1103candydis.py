def distribute(candies,people):
    list1=[0 for x in range(people)]
    list2=[]
    for x in range(people):#0 1 2 3 4 5 6 
        list3=[]
        for y in range(x+1):
            list3.append(y+1)
        list2.append(list3)
    print(list2)
distribute(7,4) 
#incompleted