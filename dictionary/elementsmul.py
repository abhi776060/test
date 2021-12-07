class MulElements:
    def __init__(self,dict1):
        self.new_dict1=dict1

    def mulall(self):
        sum=1
        for x in self.new_dict1.values():
            sum*=x
        return sum
 
    
dict1={'key1':1,'key2':2}
me=MulElements(dict1)
print(me.mulall())