class KeyType():
    def show(self,my_dict):
        new_dict={}
        for key, value in my_dict.items():
            if type(value) is str:
                new_dict[key]='str'
            elif type(value) is int:
                new_dict[key]='int'
            elif type(value) is float:
                new_dict[key]='float' 
        return new_dict

me=KeyType()
my_dict={'name':'abhishek','age':26,'price':25.8}
print(me.show(my_dict))