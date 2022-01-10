#print the following integers with zeros on the left of specified width
class String:
    def __init__(self):
        pass

    def prefix(self,str1,num):
        str2=str(str1)
        if num == len(str2):
            print(str1)
        else:
            str3=''
            for x in range(num-len(str2)):
                str3+='0'
            str4=str3+str2
            print(str4)

solution=String()
solution.prefix(6000,6)