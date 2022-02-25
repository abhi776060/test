def serviceLane(n, cases):
    # Write your code here
    service_lane_width={key:val for key,val in enumerate(n)}
   
    
    list2=[]
    for i in cases:
        list1=[]
        for j in range(i[0],i[1]+1):
            list1.append(service_lane_width[j])
        list2.append(min(list1))
    print(list2)

serviceLane([2, 3, 1, 2, 3, 2, 3, 3],[[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]])