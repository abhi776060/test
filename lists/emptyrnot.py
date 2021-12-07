class Empty():
    def empty(self,list1):
        if list1:
            return "not an empty list"
        else:
            return "empty one"
    
me=Empty()
list1=[]
print(me.empty(list1))