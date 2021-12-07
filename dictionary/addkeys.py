class AddKey:
    def __init__(self,new_dict):
        self.new_dict=new_dict
    
    def add(self,key,value):
        self.new_dict[key]=value
        return self.new_dict
            
    
my_dict={'key1':5,'key2':7.5,'key3':3,'key4':1,}
me=AddKey(my_dict)

print(me.add('key7',50))