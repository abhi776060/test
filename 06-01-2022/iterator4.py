a=','.join(['a','b','c'])
print(a)


a=','.join({'a':1,'b':2})
print(a)

a=list('python')
print(a)

a=list({'a':1,'b':2})
print(a)

#iteration protocol

x=iter([1,2,3,4])
print(next(x))
print(next(x))
print(next(x))
print(next(x))



class yrange:
    def __init__(self,n):
        self.i=0
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i< self.n:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration
y=yrange(5)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
z=yrange(10)
print(list(z))