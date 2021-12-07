class TopThree:
    def __init__(self,new_dict):
        self.new_dict=new_dict
        self.dict={}
        
    def get(self,n):
        z=0
        for i in sorted(self.new_dict.values(),reverse=True):
            z+=1
            for x,y in self.new_dict.items():
                if y==i:
                    self.dict[x]=y
            if z==3:break
                    
                    
                                 
        return self.dict

            
            
        
dict1 ={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

me=TopThree(dict1)
print(me.get(3))

