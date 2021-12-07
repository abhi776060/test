class MaxNum:
    def __init__(self,new_dict):
        self.new_dict=new_dict
        
    def max_num(self):
        max_value = None
        for key in self.new_dict.keys():
            if max_value is None or max_value < self.new_dict[key]:
                max_value = self.new_dict[key]
                max_key = key
        return max_value





my_dict={'key1':5,'key2':7.5,'key3':3,'key4':100,}
me=MaxNum(my_dict)

print(me.max_num())