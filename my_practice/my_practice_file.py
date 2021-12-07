class Employee:
    initial=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Employee.initial+=1
    def get_greeting(self):
        print(self.name,self.age)
    @classmethod
    def get_class(cls):
        print(Employee.initial)
my_list={'Abhi':25,"Rak":24}
for x,y  in my_list.items():
    obj = Employee(x,y)
    obj.get_greeting()
