#lowercase first n characters in a string
'''
ABHISHEK---abhiSHEK
'''
class String:
    def __init__(self):
        pass


    def lower_n(self,str1,lower_len):
        str2=''
        for x in range(len(str1)):
            if x <lower_len:
                str2+=str1[x].lower()
            else:
                str2+=str1[x]
        print(str2)


solution=String()
solution.lower_n('ABHISHEK',4)