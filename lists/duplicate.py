class Duplicate():
    def small(self,list1):
        my_list=[]
        for x in list1:
            if x not in my_list:
                my_list.append(x)
            else:
                pass
        return my_list
me=Duplicate()
list1=[1,2,4,2,4,9]
print(me.small(list1))