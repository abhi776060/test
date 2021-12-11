class MyString:
    def add_last_char_multiply(self,str1):
        str2=str1[-2:]
        return str1+(str2*2)


me= MyString()
print(me.add_last_char_multiply('abhishek'))