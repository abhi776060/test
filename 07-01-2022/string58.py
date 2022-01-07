#move spaces to the front of a given string
class String:
    def __init__(self):
        pass

    def move_spaces(self,str1):
        str2=''
        for x in str1:
            if x ==" ":
                str2=x+str2
            else:
                str2+=x
        print(str2)

solution=String()
solution.move_spaces('abh shek k s')