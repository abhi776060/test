def fun1(x,y):
    if x==0:
        return y
    else :
        return fun1(x-1,x+y)
result=fun1(5,6)
print(result)
