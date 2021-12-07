class SumAll:
    def __init__(self,new_dict):
        self.new_dict=new_dict
        
        
    def sum_of_nesteddict(self):
        sum = 0
        for key,value in self.new_dict.items():
            for key1,value1 in value.items():
                sum+=value1
        return sum
            
            
my_dict={1:{'a1':1, 'a2':2},  
         2:{'b1':4, 'b2':5},  
         3:{'c1':7, 'c2':8}}
me=SumAll(my_dict)

print(me.sum_of_nesteddict())