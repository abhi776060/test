class myDict1:
    def __init__(self,a,b):
       self.a=a
       self.b=b
    def show(self):
        for key, value in self.a.items() & self.b.items():
            print(f'{key} values  is present in both x and y')
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
md = myDict1(x,y)
print(md.show())