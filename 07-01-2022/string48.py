#swap comma and dot in a string
class String:
    def __init__(self):
        pass

    def replace_comma_dot(self,str1):
        str2=''
        for x in str1:
            if x == ",":
                str2+='.'
            else:
                str2+=x
        print(str2)


solution=String()
solution.replace_comma_dot("abhishek,k,s")