#remove leading zeros from an IP address
'''
100.020.003.400--1.20.3.400
'''

class String:
    def __init__(self):
        pass

    def remove_leading_zero(self,str1):
        str2=''
        for x in str1.split('.'):
            y=int(x)
            str2+=str(y)+'.'
        print(str2)

solution=String()
solution.remove_leading_zero('100.020.003.400')