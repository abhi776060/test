#program to create a Caesar encryption

class String:
    alpha_list=[chr(x) for x in range(97,97+26)]*2
    def __iniyt__(self):
        pass

    def caesar_encryption(self,str1,ind):
        str2=''
        for x in str1:
            a=self.alpha_list.index(x)
            a=a+ind
            str2+=self.alpha_list[a]
        print(str2)

solution=String()
solution.caesar_encryption('abc',2)