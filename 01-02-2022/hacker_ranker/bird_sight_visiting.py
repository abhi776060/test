def migratoryBirds(arr):
    # Write your code here
    visiting_data={}
    for x in arr:
        if x in visiting_data:
            visiting_data[x]+=1
        else:
            visiting_data[x]=1
    ar=dict(sorted(visiting_data.items(),key=lambda x: x[1],reverse=True))
    return(list(ar.keys())[0])
    
# migratoryBirds([4,1,1,2,2,3,4,4,4])
migratoryBirds([1 ,2 ,3, 4 ,5 ,4 ,3, 2, 1 ,3 ,4])