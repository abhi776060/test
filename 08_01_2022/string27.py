#remove existing indentation from all of the lines in a given text
'''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
'''
class String:
    def __init__(self):
        pass

    def remove_indentation(self,str1):
        list1=[]
        for x in str1.split("    "):
            list1.append(x)
        str2=''
        for x in list1:
            if x == '\n':
                pass
            else:
                str2+=x
        print(str2)


solution=String()
strings='''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
solution.remove_indentation(strings)