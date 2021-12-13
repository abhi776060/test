class List():
    def common_element(self,list1,list2):
        l1=[]
        for x in list1:
            for y in list2:
                if x==y:
                    l1.append(x)

        return l1
me=List()

list1=[1,2,3,4,5]
list2=[4,5,7,8,9]

print(me.common_element(list1,list2))
