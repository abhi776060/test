#to add a prefix text to all of the lines in a string
class String:
    def __init__(self):
        pass

    def prefix(self,str1,prefix_ele):
        list1=[]
        for x in str1.split("\n"):
            list1.append(x)
        str2=''
        for x in list1:
            str2+=prefix_ele+x+'\n'
        print(str2)

sollution=String()
strings='''Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java.'''
sollution.prefix(strings,'#')