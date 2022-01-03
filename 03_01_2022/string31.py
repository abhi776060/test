#print the following floating numbers upto 2 decimal places with a sign

'''  input      outout
    '-2.33333'-----2.33
'''
class String:
    def __init__(self):
        pass


    def twodecimal(self,str1):
        str2=''
        if "." in str1:
            index_pos=str1.index(".")
            break_at=index_pos+2
            for x in range(len(str1)):
                if x <=break_at:
                    str2 += str1[x]
        else:
            print(str1)
        print(str2)
string1=String()
string1.twodecimal("-3.2565")