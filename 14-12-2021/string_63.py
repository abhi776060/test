#compute sum of digits of a given string
class String:
    def __init__(self):
        pass

    def leading_zeros(self,str1):
        str2=''
        lis1=[]
        for x in str1.split('.'):
            lis1.append(int(x))
        for x in lis1:
            str2=str2+'.'+str(x)
        return str2
me=String()
print(me.leading_zeros('001.200.001.004'))
