class SwapChar():
    def __init__(self,str1):
        self.str1=str1
    def swap(self,str2,str3):
        str4=''
        for x in self.str1:
            if x == str2:
                str4+=str3
            else:
                str4+=x
        return str4

me=SwapChar("abhishek")
print(me.swap('i','o'))