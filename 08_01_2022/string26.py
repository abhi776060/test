#display formatted text (width=50) as output
class String:
    def __init__(self):
        pass

    def formated_text_width(self,str1):
        fivty_tables=[x for x in range(1,10000) if x%50==0]
        str2=''
        for x in range(len(str1)):
            if x in fivty_tables:
                str2+=str1[x]+'$'
            else:
                str2+=str1[x]
        letter_list=[]
        for x in str2.split('$'):
            letter_list.append(x)
        str3=''
        for x in letter_list:
            str3+=x+'\n'
        print(str3)
solution=String()
string1='''Python is a widely used high-level, general-purpose,interpreted,dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.'''
solution.formated_text_width(string1)