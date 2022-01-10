#print the following floating numbers with no decimal places
'''
x = 3.1415926
y = -12.9999
'''
class String:
    def __init__(self):
        pass

    def round(self,str1):
        index=str1.index('.')

        if str1[0]=="-":
            number = int(str1[:index])
            decimal = int(str1[index + 1])

            if decimal < 5:
                pass
            else:
                number -= 1
            print(number)
        else:
            number=int(str1[:index])
            decimal=int(str1[index+1])

            if decimal <5:
                pass
            else:
                number+=1
            print(number)

solution=String()
solution.round("-3.41415926")
'''
-1 0 1 '''