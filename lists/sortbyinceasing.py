class List():
    def len_2(self,list1):
        list2=[x for x in sorted(list1)]

        return list2

me=List()
list1=[5,7,5,9,3,8,8,5,6]
print(me.len_2(list1))
