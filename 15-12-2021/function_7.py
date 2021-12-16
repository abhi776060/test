#table of the given number

class Function:
    def __init__(self):
        pass
    def fabinacci(self,num):
        for i in range(1,11):
            print(f'{num} * {i}= { num*i}')
me=Function()
print(me.fabinacci(2))