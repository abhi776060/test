class Decimal:
    def decy(self,str1,n):
        self.str1=str1
        list1=[]
        list2=[]
        for x in self.str1:
            list1.append(x)
            if x=='.':
                break
        for y in self.str1[len(list1):n+3]:
            list2.append(y)
        list3=list1+list2
        str3=''
        for z in list3:
            str3+=z
        return str3



        


str1='25.6451'
me=Decimal()
print(me.decy(str1,2))
