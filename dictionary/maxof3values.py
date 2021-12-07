class MaxThreeValue:
    def __init__(self,new_dict):
        self.new_dict=new_dict
        
        
    def max_num(self):
        max_value = []
        for value in sorted(self.new_dict.values(),reverse=True):
            max_value.append(value)
            
        return max_value[:3]





my_dict={'key1':5,'key2':7.5,'key3':3,'key4':100,}
me=MaxThreeValue(my_dict)

print(me.max_num())