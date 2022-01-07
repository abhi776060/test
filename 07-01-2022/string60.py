#capitalize first and last letters of each word of a given string
class String:
    def __init__(self):
        pass

    def capitalize_first_lats(self,str1):
        str2=''
        for x in range(len(str1)):
            if x == 0 or x == len(str1):
                str2+=str1[x].upper()
            else:
                str2+=str1[x]
        print(str2)

solution = String()
solution.capitalize_first_lats("abhishek")