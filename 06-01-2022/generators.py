def yrange(n):
    i=0
    while i<n:
        yield i
        i+=1
y=yrange(5)
print(list(y))

def range(i,n,s):
    i=0
    while i<n:
        if i %s ==0:
            yield i
        i+=1
s=range(1,10,3)
print(list(s))
