def miniMaxSum(arr):
    # Write your code here
    filter_list=[]
    i=0
    j=len(arr)
    while i<len(arr):
        a=arr.copy()
        del a[i]
        
        filter_list.append(sum(a))
        i+=1
    filter=sorted(filter_list)
    print(filter[0],filter[-1])
miniMaxSum([1,2,3,4,5])