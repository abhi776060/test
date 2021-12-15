#to match the item in two dictionaries.
class Function:
    def __init__(self):
        pass
    def check_key_value(self,dict1,dict2):
        dict3={}
        for x,y in dict1.items():
            for i,j in dict2.items():
                if x==i and y==j:
                    dict3[x]=y
                else:pass
        for x in dict3.items():
            return dict3,"key and values are same"
        return 'no matching key and value'

me=Function()
dict1={'key':1,'key2':2}
dict2={'key1':9,'key2':20}
print(me.check_key_value(dict1,dict2))