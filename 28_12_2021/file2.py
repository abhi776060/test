#Write a Python program to read first n lines of a file
'''

display only specified charetors
'''
class File:
    def __init__(self):
        pass


    def read_line(self,file,line):
        with open(file,'r') as f:
            for x in range(line):
                print(f.readline())

file1=File()
file1.read_line('test1.txt',2)