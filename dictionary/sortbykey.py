class SortDict:
    def __init__(self,new_dict):
        self.new_dict=new_dict
        self.dict={}
        #print(self.new_dict)
        #print(self.dict)
    


    def get_key(self):
            for i,j in sorted(self.new_dict.items()):
                self.dict[i]=j
            return self.dict
my_dict={'key9':5,'key1':7.5,'key8':3,'key5':1,}
me=SortDict(my_dict)

print(me.get_key())