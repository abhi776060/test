class List():
    def copy_list(self,list1):

        list2=[x for x in list1]
        print('address of 2nd list',id(list2))

me=List()

list1=[5,7,5,9,3,8,8,5,6]
print('address of 1st list',id(list1))
print(me.len_2(list1))
