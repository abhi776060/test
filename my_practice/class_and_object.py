class MyBook:

    def __init__(self):
        self.name='hai'

    def set_name(self,name):
        self.name = name


book1 = MyBook()
book2 = MyBook()

book1.set_name('hai')
#book2.set_name('loo')

print(book1.name)
print(book2.name)
