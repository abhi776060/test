class Exist:
    def __init__(self,new_dict):
        self.new_dict=new_dict
    
    def exist(self,key):
        if key in self.new_dict:
            return "keys present"
        return "key not present"
            
    
my_dict={'key1':5,'key2':7.5,'key3':3,'key4':1,}
me=Exist(my_dict)

print(me.exist('key10'))