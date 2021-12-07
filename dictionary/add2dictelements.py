class AddSameKayValues:
    def __init__(self,dict1,dict2):
        self.new_dict1=dict1
        self.new_dict2=dict2
        self.dict={}
               

    def add_samekey(self):
        for key,value in self.new_dict1.items():
            if key in self.new_dict2:
                for i,j in self.new_dict2.items():
                    if i == key:
                        self.dict[key]=value+j
                    else:
                        self.dict[i]=j
                    
            else:
                self.dict[key]=value
                

       

        return self.dict


 
    
dict1={'key1':1,'key2':2}
dict2={'key2':3,'key4':4}
me=AddSameKayValues(dict1,dict2)

print(me.add_samekey())