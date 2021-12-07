class Lose:
    def __init__(self):
        
        self.dict={}
    def my_fun(self,list1,list2):
        for key,value in zip(list1,list2):
            if key not in self.dict:
                self.dict[key]=value
            else:
                self.dict[key].value
        return self.dict
first_list=[1,2,3,4,5,6]
second_list=[1,1,1,1,1,1]
me=Lose()
print(me.my_fun(first_list,second_list))