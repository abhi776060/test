class Iterate:
    def __init__(self,my_set):
        self.new_set=my_set

    
    def itarate(self):
        for i in self.new_set:
            print(f'{i} iteration:',i)
              
    
myset={1,2,3,4,5,6,7,8,9}
me=Iterate(myset)

print(me.itarate())