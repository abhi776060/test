#print the following integers with '*' on the right of specified width
class String:
    def __init__(self):
        pass

    def right_padding(self,str1,width):
        if len(str1)>=width:
            print(str1)
        else:
            str2=''
            for x in range(width-len(str1)):
                str2+="*"
            str3=str1+str2
            print(str3)



solution=String()
solution.right_padding('123',5)