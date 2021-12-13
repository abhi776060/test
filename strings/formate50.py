class MyString:
    def formate_50(self,str1):
        str2=''
        for x in range(50):
            str2+=' '
        str2+=str1
        return str2

me= MyString()
print(me.formate_50('abhishek'))