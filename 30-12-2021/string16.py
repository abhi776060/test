#Insert string in middle of speical chars
class String:
    def __init__(self):
        pass
    def insert_middle(self,str1,chr1):
        a=len(str1)//2
        print(str1[:a]+chr1+str1[a:])

string1=String()
string1.insert_middle("abhishek",'@')