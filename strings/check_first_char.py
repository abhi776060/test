class MyString:
    def __init__(self,str2):
        self.str2=str2
    def check_first_char(self,str1):
        if self.str2[0] == str1[0]:
            print('Yes')
        else:
            print('No')
me= MyString('abhishek')
print(me.check_first_char('b'))