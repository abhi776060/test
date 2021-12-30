#nth index character from string
class String:
    def __init__(self):
        pass
    def index(self,str1,chr1):
        for x in range(len(str1)):
            if str1[x]==chr1:
                print(x)


string1=String()
string1.index("abhishek",'k')