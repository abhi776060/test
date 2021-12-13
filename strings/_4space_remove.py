class MyString:
    def remove_indentetion(self,str1):
        str2=''
        str3=str1.replace('    ',' ')
        return str3
strn='''    abhishek abhishek abhishek 
    abhishek abhishek'''
me= MyString()
print('origional::',strn)
print('updated::',me.remove_indentetion(strn))