class Generate:
    def __init__(self):
        self.new_set=set()

    
    def generate(self,n):
        for i in range(1,n+1):
            self.new_set.add(i)

        return self.new_set  
    

me=Generate()

print(me.generate(10))