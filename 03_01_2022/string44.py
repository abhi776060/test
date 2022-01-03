#print the index of the character in a string
'''
abhi
a at 0 index
b at 1 index
h at 2 index
i at 3 index
'''
class String:
    def __init__(self):
        pass

    def find(self,str1):
        for x in range(len(str1)):
            print(f'{str1[x]} at {x} index')

string1=String()
string1.find("abhi")