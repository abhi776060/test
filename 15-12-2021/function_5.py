#convert list/tuple/set to list/tuple/set


class Function:
    def __init__(self):
        pass
    def square_cube(self,num):
        if type(num)==list:
            print(tuple(num))
            print(set(num))
        elif type(num)==tuple:
            print(list(num))
            print(set(num))
        elif type(num)==set:
            print(list(num))
            print(tuple(num))
        else:
            print("please provide set or list or tuple only")
me=Function()
print(me.square_cube('sfjhuf'))