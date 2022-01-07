# reverses a string if it's length is a multiple of 4
class String:
    def __init__(self):
        pass
    def reverse_char_if_len4(self,str1):
        str2=''
        if len(str1)%4 == 0:
            for x in str1:
                str2=x+str2
        else:
            print(str1)
        print(str2)

solution=String()
solution.reverse_char_if_len4("abhishek")