class CharAppend():
    def __init__(self,str1):
        self.str1=str1
    def append_char(self,str2):
        str4=''
        str4=self.str1+str2
        return str4


me=CharAppend("abhishek")
print(me.append_char('a'))