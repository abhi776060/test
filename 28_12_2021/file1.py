#  Write a Python program to read an entire text file
'''

read file as it in txt
'''

class File:
    def __init__(self):
        pass


    def read_file(self,pointer):
        if '.txt' not in pointer:
            input = pointer + '.txt'

        else:
            input = pointer
        with open(input,'r') as f :
            print(f.read())

file=File()
user=input(" enter txt file name")
file.read_file(user)