class List():
    def len_2(self,list1):
        count=0
        for x in list1:
            if len(x)==2:
                count+=1
        return count

me=List()
list1=['abhishek','a','aaa','aa','sd','we']
print(me.len_2(list1))
