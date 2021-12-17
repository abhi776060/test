#print even and odd numbers

class Function:
    def __init__(self):
        pass
    def even_odd(self,num):
        even=[]
        odd=[]
        for x in num:
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
        return f'even :{even}, odd :{odd}'
me=Function()
print(me.even_odd([1,2,3,4,5,6,7]))