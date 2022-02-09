def utopian(n):
    growth=[]
    first=1
    second=2
    for x in range(0,n+1,2):
        growth.append(first)
        growth.append(second)
        first=second+1
        second=first*2
    return(growth[n])
print(utopian(5))