class SortDict:
    def __init__(self,new_dict):
        self.new_dict=new_dict
        self.dict={}
        #print(self.new_dict)
        #print(self.dict)

    def get_value(self):
            for i in sorted(self.new_dict.values()):
                for x,y in self.new_dict.items():
                    if i==y:
                        self.dict[x]=i
            return self.dict
my_dict={'key1':5,'key2':7.5,'key3':3,'key4':1,}
me=SortDict(my_dict)

print(me.get_value())