#reverse a string
class String:
    def __init__(self):
        pass


    def reverse(self,str1):
        str2=''
        for x in str1:
            str2=x+str2
        print(str2)

solution=String()
solution.reverse("abhishek")