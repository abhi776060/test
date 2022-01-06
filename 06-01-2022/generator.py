def integer():
    i=0
    while True:
        yield i
        i+=1
def square():
    for x in integer():
        yield x*x
def take(x,y):
    sec=x()
    result=[]
    try:
        for i in range(y):
            result.append((next(sec)))
    except:
        pass
    return result
print(take(square,10))