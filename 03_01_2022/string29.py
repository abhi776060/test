#to set the indentation of the first line
'''
sample_text =
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.\
output=
Python is a widely used high-level, general-purpose, interpreted, dynamic
    programming language. Its design philosophy emphasizes code readability,
    and its syntax allows programmers to express concepts in fewer lines of
    code than possible in languages such as C++ or Java.\
'''

class String:
    def __init__(self):
        pass

    def indent(self,str1):
        str2=''
        for x in str1:
            if x == "\n":
                str2=str1.replace('\n','\n    ')
        print(str2)



string1=String()
simple_text='''Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.'''
string1.indent(simple_text)