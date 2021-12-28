#Write a Python program to append text to a file and display the text

class File:
    def __init__(self):
        pass

    def add(self,file,text):
        with open(file,'a') as f:
            f.write(text)
        with open(file,'r') as f:
            print(f.read())




file1=File()
x=input(" enter your text")
file1.add('test1.txt', x)