def cutTheSticks(arr):
    # Write your code here
    aar1=arr
    list2=[]
    for x in range(len(aar1)):
        
        if len(aar1)==0:
            break
        min_num=min(aar1)
        list1=[]
        list2.append(len(aar1))
        for y in range(len(aar1)):
            y=aar1[y]-min_num
            if y:
                list1.append(y)
        aar1=list1
    print(list2)
    
cutTheSticks([5,4,4,2,2,8])
        