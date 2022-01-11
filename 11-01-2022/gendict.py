class PrintDict:
    def __init__(self):
        self.new_dict={}

    
    def printing_1_15(self,n):
        for i in range(1,n+1):
            self.new_dict[i]=i*i
        return self.new_dict  
    

me=PrintDict()

print(me.printing_1_15(15))