class List():
    def remove_by_index(self,list1,n):
        l1=[]
        for x in list1:
            if list1.index(x)==n:
                pass
            else:
                l1.append(x)
        return l1
me=List()
list1=[1,2,3,4,5]

print(me.remove_by_index(list1,3))#index
