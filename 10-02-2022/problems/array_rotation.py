from operator import le


def circularArrayRotation(a, k, queries):
    # Write your code here
    new_a=a
    i=0
    list1=[]
    for x in range(k+1):
        print(new_a)
        new_a=new_a[:len(new_a-1)]+new_a[:1]
        i+=1
        if k ==i:
            for x in queries:
                list1.append(new_a[x])
    return list1
# circularArrayRotation([3,4,5],2,[1,2])
print(circularArrayRotation([1,2,3],3,[0,1,2]))

