#to format a number with a percentage
'''
0.25-----25%
'''

class String:
    def __init__(self):
        pass

    def percentage(self,str1):
        i=str1.index(".")
        x=str1[i+1:i+3]
        y=str1[i+3:]
        z=x+'.'+ y
        print(f'{z}%')

string1=String()
string1.percentage('0.76')