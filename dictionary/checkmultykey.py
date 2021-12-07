class Exist:
    def __init__(self,new_dict):
        self.new_dict=new_dict
    
    def exist(self,*key):
        for x in key:
            if x in self.new_dict:
                print(f"{x}key present")
            else:
                print(f"{x}key not present")
            
    
my_dict={'key1':5,'key2':7.5,'key3':3,'key4':1,}
me=Exist(my_dict)

print(me.exist('key1','key10'))