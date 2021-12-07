class MurgeDict:
    def __init__(self,dict1,dict2):
        self.new_dict1=dict1
        self.new_dict2=dict2

    def murge(self):
        self.new_dict1.update(self.new_dict2)
        return self.new_dict1
 
    
dict1={'key1':1,'key2':2}
dict2={'key3':3,'key4':4}
me=MurgeDict(dict1,dict2)

print(me.murge())