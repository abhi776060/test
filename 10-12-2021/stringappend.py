class MyString():
    def __init__(self,str1):
        self.str1=str1
    def append_string(self,str2):
        str4=''
        str4=self.str1+str2
        return str4


me=MyString("abhishek")
print(me.append_string('ahhd'))