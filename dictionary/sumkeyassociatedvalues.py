class SumKeyAssociatedValues:
    def __init__(self,dict1):
        self.new_dict1=dict1

    def sumall(self):
        sum_num=0
        for x in self.new_dict1.keys():
            for y in x:
                if y.isdigit():
                    sum_num+=int(y)
            
        return sum_num
 
    
dict1={'key1':1,'key2':2,'key8':78}
me=SumKeyAssociatedValues(dict1)
print(me.sumall())