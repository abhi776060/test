class TwoListToDict:
    def __init__(self,list1,list2):
        self.list1=list1
        self.list2=list2
        
    def print_dict(self):
        dict1 = {}
        try:
            for key in self.list1:
                for value in self.list2:
                    dict1.add(value)
                    self.list2.remove(value)
                    break
            return dict1
        except Exception as e:
            print(" methods not found  ")
 
list1=[1,2,3,4]
list2=[1,2,3,4]

me=TwoListToDict(list1,list2)
me.print_dict()
