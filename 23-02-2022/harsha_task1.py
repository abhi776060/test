def sum_same_num(a):
    dict1={}
    for x in a :
        if x not in dict1:
            dict1[x]=1
        else:
            dict1[x]+=1
    sum=0
    for key,val in dict1.items():
        sum=key**val
        print(sum)
    print(sum)

sum_same_num([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6])