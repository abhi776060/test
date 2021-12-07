class StringToDict:
    def __init__(self):
        self.dict={}

    def printing(self,mystring):
        
        for i in mystring:
            if i in self.dict:
                self.dict[i]+=1
            else:
                self.dict[i]=1
        return self.dict 
    

me=StringToDict()

print(me.printing("abhishek"))