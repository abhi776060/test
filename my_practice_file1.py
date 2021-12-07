class MyClass:
    def method(self):
        return 'instance method called'

    @classmethod
    def classmethod(cls):
        return 'class method called'

    @staticmethod
    def staticmethod():
        return 'static method called'
print(MyClass.staticmethod())
#b=MyClass()
#print(b.staticmethod())