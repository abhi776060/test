class Human:
    def __init__(self,age,name):
        self.name=name
        self.age=age


class Dance:
    def __init__(self,style):
        self.style=style

class Student(Human,Dance):
    def __init__(self,age,name,style):
        Human.__init__(self,age,name)
        Dance.__init__(self,style)
john=Student(25,'John','hiphop')
print(john.name)
print(john.age)
print(john.style)
