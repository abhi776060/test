#Write a Python program to read a file line by line and store it into a list
from time import sleep
class File:
    def __init__(self):
        pass

    def read_line_by_line(self, file):
        lis=[]
        with open(file, 'r') as f:
            for x in f.read().split('\n'):
                lis.append(x)
                print(x)
                sleep(2)
        print(lis)


file1 = File()
file1.read_line_by_line('test1.txt')