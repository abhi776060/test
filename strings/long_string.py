class MaxLenString():
    def MaxLen(self,mylist):
        count={}
        for c in mylist:
            f=0
            for x in c:
                f+=1
            count[c]=f
        my_new_list=list(count.values())
        max_num=my_new_list[0]            
        for x in my_new_list:
            if x > max_num :
                max_num = x
        for x,y in count.items():
            if y==max_num:
                return x
me=MaxLenString()
list1=['abhishek','rakesh','vijhdfgdyshnu']
print(me.MaxLen(list1))
