def pageCount(n, p):
    # Write your code here
    mid=n//2
    flag=[]
    if mid < p:
        flag=list(reversed([(x,x+1) for x in range(0,n+1,2)]))
    else:
        flag=[(x,x+1) for x in range(0,n+1,2)]

    count=0
    for x in flag:
        print(x)
        if p in x:
            break
        count+=1
    return(count)
print(pageCount(6,2))


