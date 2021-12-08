class Currencydigits:
    def fun(self,str1):
        list1=[]
        if '.' not in str1:
            list1.append('.')
        for x in list1:
            list1.append(x)
        return list1

            
me=Currencydigits()
print(me.fun('123456789'))
