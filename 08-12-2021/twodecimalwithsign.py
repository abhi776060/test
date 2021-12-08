class Decimal:
    def decy(self,str1,n):
        self.str1=str1
        list1=[]
        for x in self.str1:
            list1.append(x)
        for y in list1:
            if y=='.':
                z=list1.index(y)
        list2=list1[:z+1]+list1[z+1:z+1+n]
        str2=''
        for z in list2:
            str2+=z
        return str2
str1='-25.6451'
me=Decimal()
print(me.decy(str1,2))
