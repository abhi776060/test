class UnicValues:
    def __init__(self,dict1,dict2):
        self.new_dict1=dict1
        self.new_dict2=dict2
               

    def unic(self):
        temp=set()
        
        for key,value in self.new_dict1.items():
            for i,j in self.new_dict2.items():
                    if value== j:
                        temp.add(value)
          

        return f"unique values are {list(temp)}"
   
dict1= {'key1':1,'key2':2}
dict2={'key2':1,'key4':2}
me=UnicValues(dict1,dict2)

print(me.unic())
