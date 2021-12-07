class ToNestedList:
    def __init__(self,list1):
        self.list1=list1
    
    def nested(self):
        new_dict = current = {}
        for name in list1:
            current[name] = {}
            current = current[name]
        return new_dict
            
    
list1=[1, 2, 3, 4]
me=ToNestedList(list1)

print(me.nested())