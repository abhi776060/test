class Person:
    def __init__(self,name):
        self.name=name
    def say_name(self):
        print("my name is ",self.name)
person1=Person('abhi')
person1.say_name()