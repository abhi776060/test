class MaxNum:
    def __init__(self,new_dict):
        self.new_dict=new_dict
        self.dict={}
        
    def max_num(self):
        temp = []
        for key, val in self.new_dict.items():
            if val not in temp:
                temp.append(val)
                self.dict[key] = val

        return self.dict





my_dict={'key1':5,'key2':7.5,'key3':5,'key4':100,}
me=MaxNum(my_dict)

print(me.max_num())