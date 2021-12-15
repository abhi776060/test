# function to display group of strings
class Function:
    def __init__(self):
        pass
    def display_group_string(self):
        lis1=[]
        i=1
        while i:
            words = input(" enter strings :")
            i=int(input('1 for continue 0 for exit'))
            lis1.append(words)
        return lis1



me=Function()

print(me.display_group_string())