#Generator Expression

a=(x for x in range(10))
print(list(a))

b=sum((x for x in range(1,10)))
print(b)
import itertools
for x,y in zip(['a','b','c'],[1,2,3]):
    print(x,y)