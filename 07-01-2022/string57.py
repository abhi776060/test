#remove spaces from a given string
class String:
    def __init__(self):
        pass

    def remove_spaces(self,str1):
        str2=''
        for x in str1:
            if x == " ":
                pass
            else:
                str2+=x
        print(str2)

solution=String()
solution.remove_spaces("abhi shek")