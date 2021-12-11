class Replace_first_accurence:
    def __init__(self):
        pass
    def first_accurence(self,str1,m,n):
        str2=''
        for i in str1:
            if i == str1[n]:
                str2+=m
            else:
                str2+=i
        return str2

me=Replace_first_accurence()
print(me.first_accurence('abhishek','k',5))
