# Write a Python program to read last n lines of a file
from time import sleep
class File:
    def __init__(self):
        pass

    def add(self,file,text):
        start=-text
        with open(file,'r') as f:
            line=f.read().split("\n")
            for x in line[start:]:
                print(x)
            





file1=File()
file1.add('test1.txt', 2)