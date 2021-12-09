class Exist:
    def __init__(self,new_dict):
        self.new_dict=new_dict
    def exist(self,key):
        if key in self.new_dict:
            try:
                return key1
            except Exception as e:
                print("name error")
        

                
my_dict={'key1':5,'key2':7.5,'key3':3,'key4':1,}
me=Exist(my_dict)

print(me.exist('key2'))